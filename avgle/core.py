import requests
import json


URL = r"https://api.avgle.com/v1"

LAST_VIEWED = "bw"
LATEST = "mr"
MOST_VIEWED = "mv"
TOP_RATED = "tr"
MOST_FAVOURED = "tf"
LONGEST = "lg"

DAY = "t"
WEEK = "w"
MONTH = "m"
FOREVER = "a"

def output(url, params=None):
    req = requests.get(url, params=params)
    return json.loads(req.text)


class AvgleError(Exception):
    pass