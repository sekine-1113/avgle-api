from .videos import Videos
from .informations import Informations
from .core import Client, AvgleError, OrderBy, Date


class Avgle(Client):
    def __init__(self, cache=None, host='api.avgle.com', user_agent=None, retry_count=1, retry_delay=0, timeout=60, use_cache=True) -> None:
        super().__init__(cache, host, user_agent, retry_count, retry_delay, timeout, use_cache)

        self.videos = Videos(self)
        self.info = Informations(self)

    def get_videos(self, page=0, limit=50):
        """
        get videos by page.

        :param page (optional): integer / default 0
        :param limit (optional): interger 1~250 / default 50
        """
        return self.videos.get_videos(page, limit)


    def search_videos(self, query, page=0, limit=50,
                    o=OrderBy.LATEST, t=Date.FOREVER, tp=None, c=None):
        """
        search videos by query.

        :param query (required): string / not empty.
        :param page (optional): integer / default 0
        :param limit (optional): interger 1~250 / default 50
        :param o (optional): string / default mr
        :: bw: (Last viewed)
        :: mr: (Latest)
        :: mv: (Most viewed)
        :: tr: (Top rated)
        :: tf: (Most favoured)
        :: lg: (Longest)
        :param t (optional): string / default a
        :: t: (1 day)
        :: w: (1 week)
        :: m: (1 month)
        :: a: (forever)
        :param tp (optional): string / public or private
        :param c (optional): interger(CHID of a valid video category)
        """
        return self.videos.search_videos(query, page, limit, o, t, tp, c)


    def search_JAVs(self, query, page=0, limit=50,
                    o=OrderBy.LATEST, t=Date.FOREVER, tp=None, c=None):
        """
        search Japanese AV by query.

        :param query (required): string / not empty.
        :param page (optional): integer / default 0
        :param limit (optional): interger 1~250 / default 50
        :param o (optional): string / default mr
        :: bw: (Last viewed)
        :: mr: (Latest)
        :: mv: (Most viewed)
        :: tr: (Top rated)
        :: tf: (Most favoured)
        :: lg: (Longest)
        :param t (optional): string / default a
        :: t: (1 day)
        :: w: (1 week)
        :: m: (1 month)
        :: a: (forever)
        :param tp (optional): string / public or private
        :param c (optional): interger(CHID of a valid video category)
        """
        return self.videos.search_JAVs(query, page, limit, o, t, tp, c)


    def get_video_by_id(self, video_id: int|str):
        """
        get video by id.

        :param video_id (required): interger.
        """
        return self.videos.get_video_by_id(video_id)

    def get_video_categories(self):
        return self.info.get_video_categories()

    def get_video_collections(self, page=1):
        return self.info.get_video_collections(page)



__all__ = ["Avgle", "AvgleError", "OrderBy", "Date"]