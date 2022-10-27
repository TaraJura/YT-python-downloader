from pytube import YouTube
link = input("Enter the link of YouTube video you want to download:")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()