'''
Date: 2023-05-12 16:45:38
Author: Bruce
Description: 
'''
import requests
import csv
import time
import random
from fake_useragent import UserAgent

UA = UserAgent().random

url = "http://www.xinfadi.com.cn/getPriceData.html"

headers = {
    "headers": UA
}

r = requests.get(url, headers=headers)
r = r.json()
print(r)

with open("price.csv", mode="a+", newline="") as f:
    csv_writer = csv.writer(f)

    for iter in r["list"]:
        prodName = iter["prodName"]
        prodCat = iter["prodCat"]
        lowPrice = iter["lowPrice"]
        highPrice = iter["highPrice"]
        avgPrice = iter["avgPrice"]
        pubDate = iter["pubDate"]
        unitInfo = iter["unitInfo"]
        place = iter["place"]
        csv_writer.writerow([prodName, prodCat, lowPrice, highPrice, avgPrice, pubDate, unitInfo, place])
        print(f"Writing data {prodName}")
    time.sleep(float(format(random.uniform(0, 1), '.2f')))

print("Done")
