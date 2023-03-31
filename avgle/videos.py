from .core import Client, Date, OrderBy, AvgleError


class Videos:

    def __init__(self, client: Client) -> None:
        self.client = client


    def get_videos(self, page=0, limit=50):
        """
        get videos by page.

        :param page (optional): integer / default 0
        :param limit (optional): interger 1~250 / default 50
        """
        if not 1 <= limit <= 250:
            raise AvgleError

        return self.client.request(
            'GET', f'videos/{page}',
            endpoint_params=('limit'),
            params={'limit': limit}
        )


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
        if query == "":
            raise AvgleError("Query is empty, be must not empty")

        return self.client.request(
            'GET', f'search/{query}/{page}',
            endpoint_params=("limit", "o", "t", "type", "c"),
            params={
                "limit" : limit,
                "o" : o,
                "t" : t,
                "type" : tp,
                "c" : c,
            }
        )


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
        if query == "":
            raise AvgleError("Query is empty, be must not empty")

        return self.client.request(
            'GET', f'jav/{query}/{page}',
            endpoint_params=("limit", "o", "t", "type", "c"),
            params={
                "limit" : limit,
                "o" : o,
                "t" : t,
                "type" : tp,
                "c" : c,
            }
        )


    def get_video_by_id(self, video_id: int|str):
        """
        get video by id.

        :param video_id (required): interger.
        """
        return self.client.request(
            'GET', f'video/{video_id}'
        )
