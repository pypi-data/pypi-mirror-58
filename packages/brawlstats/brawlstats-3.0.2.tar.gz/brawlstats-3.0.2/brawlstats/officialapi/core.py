import aiohttp
import requests
import asyncio
import logging

import json
import time
import sys

from cachetools import TTLCache
from datetime import datetime

from ..errors import NotFoundError, Unauthorized, ServerError, Forbidden, RateLimitError, UnexpectedError  # , MaintenanceError
from .models import Player, Club, Members, Ranking, BattleLog, Constants
from .utils import API, bstag, typecasted

log = logging.getLogger(__name__)


class Client:
    """
    This is a sync/async client class that lets you access the Official API.

    Parameters
    ------------
    token: str
        The API Key that you can get by signing up at https://developer.brawlstars.com
    session: Optional[Session] = None
        Use a current session or a make new one. Can be ``aiohttp.ClientSession()`` or ``requests.Session()``
    timeout: Optional[int] = 30
        A timeout in seconds for requests to the API.
    is_async: Optional[bool] = False
        Setting this to ``True`` makes the client async.
    loop: Optional[event loop]
        The ``event loop`` to use for asynchronous operations. Defaults to ``None``,
        in which case the default event loop is used via ``asyncio.get_event_loop()``.
        If you are passing in an aiohttp session, using this will not work. You must set it when initializing the session.
    connector: Optional[aiohttp.TCPConnector]
        Pass in a TCPConnector for the client. Defaults to ``None``,
        If you are passing in an aiohttp session, using this will not work. You must set it when initializing the session.
    debug: Optional[bool] = False
        Whether or not to give you more info to debug easily.
    base_url: Optional[str] = None
        Sets a different base URL to make request to. Only use this if you know what you are doing.
    prevent_ratelimit: Optional[bool] = False
        Whether or not you want to wait for a small amount of time between requests to prevent being ratelimited.
        Recommended if you are performing multiple requests in a short period of time.
    """

    REQUEST_LOG = '{method} {url} recieved {text} has returned {status}'

    def __init__(self, token, session=None, timeout=30, is_async=False, **options):
        self.is_async = is_async
        self.loop = options.get('loop', asyncio.get_event_loop())
        self.connector = options.get('connector')
        self.session = session or (
            aiohttp.ClientSession(loop=self.loop, connector=self.connector) if self.is_async else requests.Session()
        )
        self.timeout = timeout
        self.prevent_ratelimit = options.get('prevent_ratelimit', False)
        self.lock = asyncio.Lock() if options.get('prevent_ratelimit') is True else None
        self.api = API(options.get('base_url'), version=1)

        self.debug = options.get('debug', False)
        self.cache = TTLCache(100, 300)  # 20 requests/min
        self.ratelimit = [20, 20, 0]  # per minute, remaining, time until reset

        self.headers = {
            'Authorization': 'Bearer {}'.format(token),
            'User-Agent': 'brawlstats/{0} (Python {1[0]}.{1[1]})'.format(self.api.VERSION, sys.version_info),
            'Accept-Encoding': 'gzip'
        }

    def __repr__(self):
        return '<OfficialAPI async={} timeout={} debug={}>'.format(self.is_async, self.timeout, self.debug)

    def close(self):
        return self.session.close()

    def _raise_for_status(self, resp, text, url):
        try:
            data = json.loads(text)
        except json.JSONDecodeError:
            data = text

        code = getattr(resp, 'status', None) or getattr(resp, 'status_code')

        if self.debug:
            log.debug(self.REQUEST_LOG.format(method='GET', url=resp.url, text=text, status=code))

        if 300 > code >= 200:
            if resp.headers.get('x-ratelimit-limit'):
                self.ratelimit = [
                    int(resp.headers['x-ratelimit-limit']),
                    int(resp.headers['x-ratelimit-remaining']),
                    int(resp.headers.get('x-ratelimit-reset', 0))
                ]
            return (data, resp)
        if code == 401:
            raise Unauthorized(url, code)
        if code == 403:
            raise Forbidden(url, code, data['message'])
        if code in (400, 404):
            raise NotFoundError(url, code)
        if code == 429:
            raise RateLimitError(url, code, int(resp.headers.get('x-ratelimit-reset')) - time.time())
        if code >= 500:
            # if data.get('maintenance'):
            #     raise MaintenanceError(url, code)
            raise ServerError(url, code)

        raise UnexpectedError(url, code, data)

    def _resolve_cache(self, url):
        data = self.cache.get(url)
        if not data:
            return None
        resp = 'Cached Data'
        if self.debug:
            log.debug('GET {} got result from cache.'.format(url))
        return (data, resp)

    async def _arequest(self, url):
        cache = self._resolve_cache(url)
        if cache is not None:
            return cache
        if self.ratelimit[1] == 0 and time.time() < self.ratelimit[2]:
            raise RateLimitError(url, 429, self.ratelimit[2] - time.time())

        try:
            async with self.session.get(url, timeout=self.timeout, headers=self.headers) as resp:
                data = self._raise_for_status(resp, await resp.text(), url)
        except asyncio.TimeoutError:
            raise ServerError(url, 503)
        else:
            self.cache[url] = data[0]

        return data

    def _request(self, url):
        cache = self._resolve_cache(url)
        if cache is not None:
            return cache
        if self.ratelimit[1] == 0 and time.time() < self.ratelimit[2]:
            time.sleep(self.ratelimit[2] - time.time())

        try:
            with self.session.get(url, timeout=self.timeout, headers=self.headers) as resp:
                data = self._raise_for_status(resp, resp.text, url)
        except requests.Timeout:
            raise ServerError(url, 503)
        else:
            self.cache[url] = data[0]

        return data

    async def _aget_model(self, url, model, key=None):
        if self.lock is not None:
            async with self.lock:
                data, resp = await self._arequest(url)
                await asyncio.sleep(1 / self.ratelimit[0])
        else:
            data, resp = await self._arequest(url)

        if model == Constants:
            if key:
                if data.get(key):
                    return model(self, resp, data.get(key))
                else:
                    raise KeyError('No such Constants key "{}"'.format(key))

        return model(self, resp, data)

    def _get_model(self, url, model, key=None):
        if self.is_async:
            return self._aget_model(url, model=model, key=key)
        data, resp = self._request(url)
        if self.prevent_ratelimit:
            time.sleep(1 / self.ratelimit[0])
        if model == Constants:
            if key:
                if data.get(key):
                    return model(self, resp, data.get(key))
                else:
                    raise KeyError('No such Constants key "{}"'.format(key))

        return model(self, resp, data)

    @typecasted
    def get_player(self, tag: bstag):
        """Get a player's stats.

        Parameters
        ----------
        tag: str
            A valid player tag.
            Valid characters: 0289PYLQGRJCUV

        Returns Player
        """
        url = '{}/{}'.format(self.api.PROFILE, tag)

        return self._get_model(url, model=Player)

    get_profile = get_player

    @typecasted
    def get_club(self, tag: bstag):
        """Get a club's stats.

        Parameters
        ----------
        tag: str
            A valid club tag.
            Valid characters: 0289PYLQGRJCUV

        Returns Club
        """
        url = '{}/{}'.format(self.api.CLUB, tag)

        return self._get_model(url, model=Club)

    @typecasted
    def get_club_members(self, tag: bstag):
        """Get the members of a club.

        Parameters
        ----------
        tag: str
            A valid club tag.
            Valid characters: 0289PYLQGRJCUV

        Returns Members
        """
        url = '{}/{}/members'.format(self.api.CLUB, tag)

        return self._get_model(url, model=Members)

    def get_rankings(self, ranking_type: str, limit: int=200, region='global', brawler=None):
        """Get the top count players/clubs/brawlers.

        Parameters
        ----------
        ranking_type: str
            The type of ranking. Must be "players", "clubs", "brawlers".
            Anything else will return a ValueError.
        limit: Optional[int] = 200
            The number of top players or clubs to fetch.
            If count > 200, it will return a ValueError.
        region: Optional[str] = "global"
            The region to retrieve from. Must be a 2 letter country code or "global".
        brawler: Optional[str|int] = None
            The brawler name or ID.

        Returns Ranking
        """
        if type(brawler) == str:
            brawler = brawler.lower()
        if brawler not in self.api.BRAWLERS and ranking_type not in ['players', 'clubs', 'brawlers']:
            raise ValueError("Please enter 'players', 'clubs' or a brawler.")
        if brawler in self.api.BRAWLERS.keys():
            brawler = self.api.BRAWLERS[brawler]

        if type(limit) != int:
            raise ValueError("Make sure 'count' is an int")
        if not 0 < limit <= 200:
            raise ValueError('Make sure limit is between 1 and 200.')

        url = '{}/{}/{}?limit={}'.format(self.api.RANKINGS, region, ranking_type, limit)
        if ranking_type == 'brawlers':
            url = '{}/{}/{}/{}?limit={}'.format(self.api.RANKINGS, region, ranking_type, brawler, limit)

        return self._get_model(url, model=Ranking)

    @typecasted
    def get_battle_logs(self, tag: bstag):
        """Get a player's battle logs.

        Parameters
        ----------
        tag: str
            A valid player tag.
            Valid characters: 0289PYLQGRJCUV

        Returns BattleLog
        """
        url = '{}/{}/battlelog'.format(self.api.PROFILE, tag)

        return self._get_model(url, model=BattleLog)

    def get_constants(self, key=None):
        """Gets Brawl Stars constants extracted from the app.

        Parameters
        ----------
        key: Optional[str] = None
            Any key to get specific data.

        Returns Constants
        """
        return self._get_model(self.api.CONSTANTS, model=Constants, key=key)

    def get_datetime(self, timestamp: str, unix=True):
        """Converts a %Y%m%dT%H%M%S.%fZ to a UNIX timestamp
        or a datetime.datetime object

        Parameters
        ----------
        timestamp: str
            A timestamp in the %Y-%m-%dT%H:%M:%S.%fZ format, usually returned by the API
            in the ``created_time`` field for example (eg. 2018-07-18T14:59:06.000Z)
        unix: Optional[bool] = True
            Whether to return a POSIX timestamp (seconds since epoch) or not

        Returns int or datetime.datetime
        """
        time = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
        if unix:
            return int(time.timestamp())
        else:
            return time
