from .core import *


class Informations:

    def get_video_categories(self):
        url = f"{URL}/categories"
        return output(url)


    def get_video_collections(self, page=1):
        url = f"{URL}/collections/{page}"
        return output(url)
