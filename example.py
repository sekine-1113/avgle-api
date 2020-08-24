import avgle

client = avgle.Avgle()

print(client.get_videos()["response"]["videos"])