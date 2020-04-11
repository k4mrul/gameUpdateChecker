#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import re
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

from main_code import grab_update_text

recipient = 'kamrulahsan06@gmail.com'
subject = 'Forza Horizon 4 Update'
file_name = 'forzaHorizon4'


site= "https://support.forzamotorsport.net/hc/en-us/sections/360000354527-Release-Notes-and-Known-Issues"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(site,headers=hdr)
page = urlopen(req).read()
soup = BeautifulSoup(page, 'html.parser')
anchorHeading = soup.find("a", attrs={'class':'article-list-link'}).text
anchorLink = soup.find("a", attrs={'class':'article-list-link'})['href']

if anchorHeading == 'FH4 Known Issues':
    anchorHeading = soup.find_all("a", attrs={'class':'article-list-link'})[1].text
    anchorLink = soup.find_all("a", attrs={'class':'article-list-link'})[1]['href']

findWord = re.compile(r'FH4 Release Notes:')
# print(anchorHeading)

grab_update_text(recipient, subject, findWord, anchorHeading, site, file_name)
