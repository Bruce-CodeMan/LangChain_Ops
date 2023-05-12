'''
Date: 2023-05-12 16:45:38
Author: Bruce
Description: 
'''
import requests
import csv
import random
from fake_useragent import UserAgent

UA = UserAgent().random

url = "http://www.xinfadi.com.cn/getPriceData.html"
