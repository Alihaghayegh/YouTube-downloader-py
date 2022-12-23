from pytube import YouTube


# This module is main function that handles the downloading
def download(link):
    youtube_object = YouTube(link)
    youtube_object = youtube_object.streams.get_highest_resolution()
    try:
        youtube_object.download()
    except:
        print("There is a problem in downloading")

    print("All Done...")


link = input("Put your link here: ")

if __name__ == "__main__":
    download(link)

# TODO: create a frontend with pyqt
