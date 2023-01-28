from avgleAPI import avgle

client = avgle.Avgle()

meta = client.get_videos(limit=1)["response"]["videos"][0]
for key in meta:
    print(key, meta[key])

print(client.get_video_categories())