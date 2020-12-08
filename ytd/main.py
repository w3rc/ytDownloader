print("Welcome to YouTube Downloader")
print("Loading...")

import pytube
import downloader

print('''
What do you want?
(1) Download YouTube Videos Manually
(2) Download a YouTube Playlist
''')

choice = input("Choice: ")

if choice == "1" or choice == "2":
    quality = input("Please choose a quality (low, medium, high, very high):")
    if choice == "2":
        link = input("Enter the link to the playlist: ")
        print("Downloading playlist...")
        downloader.download_playlist(link, quality)
        print("Download finished!")
    if choice == "1":
        links = downloader.input_links()
        for link in links:
            downloader.download_video(link, quality)
else:
    print("Invalid input! Try Again...")
