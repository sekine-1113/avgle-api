from .core import *


class Informations:


    def get_video_categories(self):
        url = "https://api.avgle.com/v1/categories"
        return output(url)


    def get_video_collections(self, page=1):
        url = f"https://api.avgle.com/v1/collections/{page}"
        return output(url)
