from pytube import YouTube

def Download():
    #youtubeObject = YouTube(link)
    
    yt = yt.streams.get_highest_resolution()
    
    
    try:
        yt.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = input("Enter the YouTube video URL: ")
yt = YouTube(link)
Download(yt)
yt = yt.streams.filter(file_extension='mp4')
