"""
動作確認はしてないが、たぶん動くのでヨシ！
"""

from .videos import Videos
from .informations import Informations

class Avgle(Videos, Informations):

    def __init__(self, page=0, limit=50):
        Videos.__init__(self, page, limit)
        Informations.__init__(self)