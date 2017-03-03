# Code by Yufei Long
import sys
import urllib2
from bs4 import BeautifulSoup
import time
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

url = ('http://www.booking.com/searchresults.html?aid=355028&sid=74d812826ea9d609b4fc585bfee42ba5&checkin=2016-12-04&checkout=2016-12-05&class_interval=1&dest_id=20088325&dest_type=city&group_adults=2&group_children=0&hlrd=0&label_click=undef&no_rooms=1&review_score_group=empty&room1=A%2CA&sb_price_type=total&score_min=0&ssb=empty&nflt=class%3D4%3B&unchecked_filter=class')
ourUrl = urllib2.urlopen(url)
soup = BeautifulSoup(ourUrl, "html.parser")
name1 = str(soup.find_all("span",{"class":"sr-hotel__name"}))
name1 = name1.replace('\n','')
name1 = name1.replace('\r','. ')
name1 = name1.replace('<span class="sr-hotel__name">\\n','')
name1 = name1.split('\\n</span>,')


score = str(soup.find_all(attrs={'class':"average js--hp-scorecard-scoreval"}))
score = score.replace('\n','')
score = score.replace('\r','. ')
score = score.replace('<span class="average js--hp-scorecard-scoreval" itemprop="ratingValue">\\n', '')
score = score.split('\\n</span>,')


with open ('four_star.txt','a') as csvfile:
    for i in range(0,15):
        csvfile.write(name1[i] + '\t' + score[i]+'\n')

