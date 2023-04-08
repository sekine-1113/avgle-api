# これは何? What is this?

これは非公式なAvgleAPIラッパーライブラリです。

This is unofficial AvgleAPI wrapper lib for Python.

# 使い方, How to use

## インストール, Install

`pip install git+https://github.com/sekine-1113/avgle-api.git`


## 使用例, example

[example.py](example.py)

```python
import avgle

client = avgle.Avgle()

print(client.videos.get_videos(limit=1)["response"]["videos"][0]['title'])
print(client.info.get_video_categories()['response']['categories'][0])
print(client.search_JAVs("AV", o=avgle.OrderBy.LATEST, t=avgle.Date.MONTH)['response']['videos'][0]['title'])

```