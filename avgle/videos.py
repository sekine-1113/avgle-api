from .core import *


class Videos:


    def get_videos(self, page=0, limit=50):
        """
        get videos by page.

        :param page (optional): integer / default 0
        :param limit (optional): interger 1~250 / default 50
        """
        url = f"{BASE_URL}/videos/{page}"
        params = {"limit" : limit}
        return output(url, params)


    def search_videos(self, query, page=0, limit=50,
                    o="mr", t="a", tp=None, c=None):
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
        if query == "":
            raise AvgleError("Query is empty, be must not empty")
        url = f"{BASE_URL}/search/{query}/{page}"
        params = {
            "limit" : limit,
            "o"     : o,
            "t"     : t,
            "type"  : tp,
            "c"     : c,
        }
        return output(url, params)


    def search_JAVs(self, query, page=0, limit=50,
                    o="mr", t="a", tp=None, c=None):
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
        if query == "":
            raise AvgleError("Query is empty, be must not empty")
        url = f"{BASE_URL}/jav/{query}/{page}"
        params = {
            "limit" : limit,
            "o"     : o,
            "t"     : t,
            "type"  : tp,
            "c"     : c,
        }
        return output(url, params)


    def get_video_by_id(self, video_id):
        """
        get video by id.

        :param video_id (required): interger.
        """
        url = f"{BASE_URL}/video/{video_id}"
        return output(url)
