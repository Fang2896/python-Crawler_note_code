import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "Referer":"https://movie.douban.com/"
}
url = "https://movie.douban.com/cinema/nowplaying/ganzhou/"


# 1. 将目标网站上的页面抓取下来
response = requests.get(url, headers=headers)
# print(response.text)
text = response.text

# 2. 将抓取下来的数据根据一定的规则进行提取
html = etree.HTML(text) # 对HTML字符串进行解析
ul = html.xpath("//ul[@class="lists]")[0]
lis = ul.xpath("./li")
for li in lis:
    title = li.xpath("@data-title")[0]
    # "..."




