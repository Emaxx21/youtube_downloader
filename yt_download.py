import pytube 

url = input("URL: ")
video = pytube.YouTube(url)
video.streams.first().download()
