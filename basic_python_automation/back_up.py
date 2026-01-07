import os
import shutil

source = "test"
destination = "backup"

os.makedirs("backup",exist_ok=True)

for file in os.listdir(source):
	shutil.copy(source+"/"+file,destination+"/"+file)

print("backup completed")
