from .core import Client


class Informations:

    def __init__(self, client: Client) -> None:
        self.client = client

    def get_video_categories(self):
        return self.client.request(
            'GET', 'categories',
        )

    def get_video_collections(self, page=1):
        return self.client.request(
            'GET', f"collections/{page}"
        )
