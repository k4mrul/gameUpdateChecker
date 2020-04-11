#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import re
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

from main_code import grab_update_text

recipient = 'kamrulahsan06@gmail.com'
subject = 'Fifa 2020 Update'
file_name = 'fifa2020'

# site= "https://www.fifaultimateteam.it/en/tag/ps4/"
site= "https://games-guides.com/tag/fifa-20/"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(site,headers=hdr)
page = urlopen(req).read()
soup = BeautifulSoup(page, 'html.parser')
anchorHeading = soup.find('h3', attrs={'class':'entry-title'}).find('a').text
anchorLink = soup.find('h3', attrs={'class':'entry-title'}).find('a')['href']
findWord = re.compile(r'Update')

grab_update_text(recipient, subject, findWord, anchorHeading, anchorLink, file_name)
