import requests
import time
from platform import python_version
from urllib.parse import urlencode

from cachetools import TTLCache

from .errors import AvgleError, BadRequest, NotFound, TooManyRequests, ServerError, HTTPException


class OrderBy:
    LAST_VIEWED = "bw"
    LATEST = "mr"
    MOST_VIEWED = "mv"
    TOP_RATED = "tr"
    MOST_FAVOURED = "tf"
    LONGEST = "lg"

class Date:
    DAY = "t"
    WEEK = "w"
    MONTH = "m"
    FOREVER = "a"


class BaseClient:

    def __init__(self, cache=None, host='api.avgle.com', user_agent=None, retry_count=1, retry_delay=0, timeout=60, use_cache=True) -> None:
        self.cache = cache or TTLCache(16, 900)
        self.host = host

        if user_agent is None:
            user_agent = (
                f"Python/{python_version()} "
                f"requests/{requests.__version__} "
                f"avgle wrapper/1.0.0"
            )
        self.user_agent = user_agent

        self.retry_count = retry_count
        self.retry_delay = retry_delay
        self.timeout = timeout

        self.use_cache = use_cache

        self.session = requests.Session()

    def request(self, method, endpoint, *, endpoint_params=(), params=None, headers=None, use_cache=True, **kwargs):
        path = f"{self.host}/v1/{endpoint}"
        url = "https://" + path
        if headers is None:
            headers = {}
        headers['User-Agent'] = self.user_agent

        if params is None:
            params = {}
        for k, arg in kwargs.items():
            if k not in endpoint_params:
                continue
            if arg is None:
                pass
            params[k] = str(arg)

        if use_cache and self.cache:
            cache_result = self.cache.get(f"{path}?{urlencode(params)}")
            if cache_result:
                self.cached_result = True
                return cache_result

        try:
            retries_performed = 0
            while retries_performed <= self.retry_count:
                try:
                    resp = self.session.request(method, url, params=params, headers=headers, timeout=self.timeout)
                except Exception:
                    raise AvgleError

                if 200 <= resp.status_code < 300:
                    break

                time.sleep(self.retry_delay)
                retries_performed += 1

            self.last_response = resp
            if resp.status_code == 400:
                raise BadRequest
            if resp.status_code == 404:
                raise NotFound
            if resp.status_code == 429:
                raise TooManyRequests
            if resp.status_code >= 500:
                raise ServerError
            if resp.status_code and resp.status_code != 304 and not 200 <= resp.status_code < 300:
                raise HTTPException

            result = resp.json()

            if use_cache and self.cache and result:
                self.cache[f"{path}?{urlencode(params)}"] = result

            return result

        finally:
            self.session.close()


class Client(BaseClient):
    pass