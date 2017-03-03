import sys
import urllib2
from bs4 import BeautifulSoup
import time
import json
import re
from urllib import urlopen
import requests
URL = ('https://www.tripadvisor.com/Hotel_Review-g60763-d6883205-Reviews-1_Hotel_Central_Park-New_York_City_New_York.html')
data = urlopen(URL)    
soup = BeautifulSoup(data, "html.parser")
n = 0
for link in soup.find_all(attrs={'class':'quote'}):
    for url_info in link.find_all('a'):
        if url_info.get('href').startswith('/ShowUserReviews'):
            url = ('https://www.tripadvisor.com' + url_info.get('href'))
            res = requests.get(url)
            res.raise_for_status()
            content = res.content
            final_soup = BeautifulSoup(content, 'html.parser')

            name = str(final_soup.find_all({'p':{'property':'reviewBody'}}))
            name = name.split('<p id="review')[1]
            name = name[36:]
            name = name.split('n</p>')[0][:-1]
            name = name.replace('<br/>','\t')
            name = name.replace('\n','')
            name = name.replace('\r','. ')
            n +=1
            print(n)
            print(name)
            with open ('1_Hotel_Central_Park_Reviews.txt','a') as csvfile:
                csvfile.write(str(n)+'\t'+str(name)+'\n')

i = 10
while i < 210:
    i= str(i)
    URL = ('https://www.tripadvisor.com/Hotel_Review-g60763-d6883205-Reviews-or' +i+'-1_Hotel_Central_Park-New_York_City_New_York.html#REVIEWS')
    data = urlopen(URL)    
    soup = BeautifulSoup(data, "html.parser")
    for link in soup.find_all(attrs={'class':'quote'}):
        for url_info in link.find_all('a'):
            if url_info.get('href').startswith('/ShowUserReviews'):
                url = ('https://www.tripadvisor.com' + url_info.get('href'))
                res = requests.get(url)
                res.raise_for_status()
                content = res.content
                final_soup = BeautifulSoup(content, 'html.parser')

                name = str(final_soup.find_all({'p':{'property':'reviewBody'}}))
                name = name.split('<p id="review')[1]
                name = name[36:]
                name = name.split('n</p>')[0][:-1]
                name = name.replace('<br/>','\t')
                name = name.replace('\n','')
                name = name.replace('\r','. ')
                n +=1
                print(n)
                print(name)
                with open ('1_Hotel_Central_Park_Reviews.txt','a') as csvfile:
                    csvfile.write(str(n)+'\t'+str(name)+'\n')
    i = int(i)
    i += 10


            




