counts = {
	"INFO":0,"WARNING":0,"ERROR":0
	}

with open("sample.log","r") as file:
	for line in file:
		for level in counts:
			if level in line:
				counts[level]+=1

print("log summary: ")
for level,count in counts.items():
	print(level,":" ,count)
