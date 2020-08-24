import requests
import json


BASE_URL = "https://api.avgle.com/v1"


def output(url, params=None):
    req = requests.get(url, params=params)
    return json.loads(req.text)
