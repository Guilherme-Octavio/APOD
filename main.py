import json
import urllib.request
import datetime
import os

API_URL = "https://api.nasa.gov/planetary/apod?api_key=Tik2BHzoXupARaIrDVUtWcAvaQC45ClIBTRtmlzb"
response = urllib.request.urlopen(API_URL)
data = json.loads(response.read())
hdimg = data['hdurl']
print(hdimg)

with open(f"images/{datetime.date.today()}.jpg", "wb") as file:
    file.write(urllib.request.urlopen(hdimg).read())
    file.close()

os.system(f"cd images && {datetime.date.today()}.jpg")


