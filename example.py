import avgle

client = avgle.Avgle()

print(client.videos.get_videos(limit=1)["response"]["videos"][0]['title'])
print(client.info.get_video_categories()['response']['categories'][0])
print(client.search_JAVs("AV", o=avgle.OrderBy.LATEST, t=avgle.Date.MONTH)['response']['videos'][0]['title'])