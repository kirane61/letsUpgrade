from pytube import YouTube

url = "https://www.youtube.com/watch?v=aBRLXvT6urs"
my_video = YouTube(url)

print("****************Video Title******************")
# Get Video title
print(my_video.title)

# Get thumbnail
print("*******************Thumbnail image***********")
print(my_video.thumbnail_url)

print("*****************Download Video***************")
# Set stream Resolution
my_video=my_video.streams.get_by_itag(22)

# for stream in my_video.streams:
#     print(stream)
my_video.download(output_path='E:/')
print("Task Completed")