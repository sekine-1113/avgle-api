from .core import *


class Videos:

    def __init__(self, page, limit):
        self._page = page
        self._params = {
            "limit" : limit,
            "o"     : "mr",
            "t"     : "a",
            "type"  : None,
            "c"     : None,
        }


    def get_videos(self, **kwargs):
        """
        get videos by page.

        :param page (optional): integer / default 0
        :param limit (optional): interger 0~250 / default 50
        """
        url = f"{BASE_URL}/videos/"
        url += f"{kwargs.get('page', self._page)}"
        return output(url)


    def search_videos(self, query, **kwargs):
        """
        search videos by query.

        :param query (required): string / not empty.
        :param page (optional): integer / default 0
        """
        if query == "":
            raise Exception("Query is empty, be must not empty")
        url = f"{BASE_URL}/search/{query}/{kwargs.get('page', self._params['page'])}"
        return output(url)


    def search_JAVs(self, query, **kwargs):
        """
        search Japanese AV by query.

        :param query (required): string / not empty.
        :param page (optional): integer / default 0
        """
        if query == "":
            raise Exception("Query is empty, be must not empty")
        url = f"{BASE_URL}/jav/{query}/{kwargs.get('page', self._params['page'])}"
        return output(url)


    def get_video_by_id(self, video_id):
        """
        search Japanese AV by query.

        :param query (required): string / not empty.
        :param page (optional): integer / default 0
        """
        url = f"{BASE_URL}/video/{video_id}"
        return output(url)
