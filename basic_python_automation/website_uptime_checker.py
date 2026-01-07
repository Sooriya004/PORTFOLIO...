import requests

url = input("enter website url: ")

try:
	r = requests.get(url,timeout=5)
	print("website is up: ",r.status_code)
except:
	print("website is down")
