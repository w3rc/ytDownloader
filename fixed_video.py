import pytube

url = 'https://www.youtube.com/watch?v=ecQ9DFv26zM&list=PLvs2R2f1Y7M5nThGXMCiHUVXeSB9O9jVA&index=3&t=1s'

video = pytube.YouTube(url)
print(video.author)

# For 720p videos
stream = video.streams.get_by_itag('22')
print("Downloading...")

stream.download(filename="test")
print("Done")

for stream in video.streams:
    if "video" in str(stream) and "mp4" in str(stream):
        print(stream)