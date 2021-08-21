from pytube import YouTube

# Taking input url from user
url = input("paste your URL here:")
output_path = input("Enter the file location you wish to save this file to: ")

# Passing the url into youtube object
yt = YouTube(url)

#To get the info of video
def get_info():
    print("Title of the video: " +yt.title)
    print("You can find the thumbnail of the video in " +yt.thumbnail_url)

# get_info()
def choose_resolution():
    print(yt.streams.filter(progressive=True))
    res = str(input("Choose the resolution you want to download from res section of above list and mention its itag here: "))
    my_video=yt.streams.get_by_itag(res)
    my_video.download(output_path=output_path)


print("-------------------------------------------------------")
get_info()
print("-------------------------------------------------------")
choose_resolution()

print("Task Completed")
