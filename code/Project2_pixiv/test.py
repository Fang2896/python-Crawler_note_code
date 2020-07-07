import requests
from bs4 import BeautifulSoup
import re, os, requests
from lxml import etree

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "referer":"https://www.pixiv.net/ranking.php"
}

baseurl='https://www.pixiv.net/ranking.php?mode=monthly&content=illust&date=20200601'


html=requests.get(baseurl, headers=headers)
with open("pixiv_rank.html", "w", encoding="utf-8") as fp:
    fp.write(html.content.decode("utf-8"))

# for i in a:
#     print(i,'\n')
#     urllist.append(i.find('img').get('data-src'))
    