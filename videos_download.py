import pytube

video_list = []

print("Enter URLs [Terminate by 'STOP']")

while True:
    url = input("")
    if url == "STOP":
        break
    video_list.append(url)

for x, video in enumerate(video_list):
    v = pytube.YouTube(video)

    # for stream in v.streams:
    #     if "video" in str(stream) and "mp4" in str(stream):
    #         print(stream)

    stream = v.streams.get_by_itag('299')
    print(f"Downloading video : {x}...")
    stream.download()
    print("Done")

