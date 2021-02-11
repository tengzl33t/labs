import os 
# This module helps in automating process of copying and removal of files and directories.
import shutil
from time import sleep

# Get my current working directory, you can change folder here
folder = os.getcwd()

# Create lists for different file formats
image_formats = ["jpg","png","jpeg","gif","webp","tiff"]
audio_formats = ["mp3","wav"]
video_formats = ["mp4","avi","webm"]
docs_formats = ["pdf","doc","ai","ait","txt","rtf"]

def init():
	# os.path.join makes your program cross-platform (linux/windows/etc) in terms of joining the path of two files/folders
	if not os.path.isdir(os.path.join(folder,"images")):
		os.mkdir(os.path.join(folder,"images"))
	if not os.path.isdir(os.path.join(folder,"audio")):
		os.mkdir(os.path.join(folder,"audio"))
	if not os.path.isdir(os.path.join(folder,"videos")):
		os.mkdir(os.path.join(folder,"videos"))
	if not os.path.isdir(os.path.join(folder,"docs")):
		os.mkdir(os.path.join(folder,"docs"))
	if not os.path.isdir(os.path.join(folder,"others")):
		os.mkdir(os.path.join(folder,"others"))

init()
while True:
	print(folder)
	files = os.listdir(folder)

	for file in files:
		if os.path.isfile(file) and file != "organizer.py":
			ext = (file.split(".")[-1]).lower()
			print(ext)
			if ext in image_formats:
				shutil.move(file,"images/"+file)
			elif ext in audio_formats:
				shutil.move(file,"audio/"+file)
			elif ext in video_formats:
				shutil.move(file,"videos/"+file)
			elif ext in docs_formats:
				shutil.move(file,"docs/"+file)
			else:
				shutil.move(file,"others/"+file)

	# delete object
	del files
	sleep(15) 
	# suspends (waits) execution of the current thread for 15 seconds
	#if program is using too much memory increase the value of sleep function