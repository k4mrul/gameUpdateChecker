#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import re
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

from main_code import grab_update_text

recipient = 'kamrulahsan06@gmail.com'
subject = 'Division 2 Update'
file_name = 'division2'

# site= "https://www.fifaultimateteam.it/en/tag/ps4/"
site= "https://www.gamerevolution.com/game/the-division-2"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(site,headers=hdr)
page = urlopen(req).read()
soup = BeautifulSoup(page, 'html.parser')
guideDiv = soup.find("div", {"id": "guides-module"})
anchorHeading = guideDiv.find_all('h4', attrs={'class':'post-listed-title'})
findWord = re.compile(r'Update')
for heading in anchorHeading:
    if 'Update' in heading.find('a').text:
        anchorHeading = heading.find('a').text
        anchorLink = heading.find('a')['href']

grab_update_text(recipient, subject, findWord, anchorHeading, anchorLink, file_name)
