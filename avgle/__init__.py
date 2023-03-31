from .videos import Videos
from .informations import Informations
from .core import Client, AvgleError, OrderBy, Date


class Avgle(Client):
    def __init__(self, cache=None, host='api.avgle.com', user_agent=None, retry_count=1, retry_delay=0, timeout=60, use_cache=True) -> None:
        super().__init__(cache, host, user_agent, retry_count, retry_delay, timeout, use_cache)

        self.videos = Videos(self)
        self.info = Informations(self)


__all__ = ["Avgle", "AvgleError", "OrderBy", "Date"]