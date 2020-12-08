import pytube

url = 'https://www.youtube.com/playlist?list=PL9a7QRYt5fqlDRSRZCtqhVCg_r5U9idbF'

playlist = pytube.Playlist(url)

for url in playlist:
    print(url)
    video = pytube.YouTube(url)
    stream = video.streams.get_by_itag('22')
    print("Downloading...")
    stream.download()
    print("Done")