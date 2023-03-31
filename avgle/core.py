import requests
import json
import time

from .errors import AvgleError


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
        self.host = host

        if user_agent is None:
            user_agent = (
                "p"
                "ython"
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

        try:
            retries_performed = 0
            while retries_performed <= self.retry_count:
                try:
                    resp = self.session.request(method, url, params=params, headers=headers, timeout=self.timeout)
                except Exception:
                    raise Exception

                if 200 <= resp.status_code < 300:
                    break

                time.sleep(self.retry_delay)
                retries_performed += 1

            self.last_response = resp

            result = resp.json()

            return result

        finally:
            self.session.close()
        return


class Client(BaseClient):
    pass