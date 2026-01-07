#copy this into the folder which has to be organised and then run it inside the folder

import os
import shutil
import sys

folder = sys.argv[1]

file_types = {
	"images":[".jpg",".png",".jpeg"], "documents":[".pdf",".txt",".docx"],"videos":[".mp4",".mkv"]
}

for filename in os.listdir(folder):
	if os.path.isfile(filename):
		moved = False
		for category, extensions in file_types.items():
			if filename.endswith(tuple(extensions)):
				os.makedirs(category,exist_ok=True)
				shutil.move(filename,category+"/"+filename)
				moved=True
		if not moved:
			os.makedirs("others",exist_ok=True)
			shutil.move(filename,"others"+"/"+filename)

print("organizing done")

