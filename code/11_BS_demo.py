from bs4 import BeautifulSoup

with open("pixiv_rank.html", "r", encoding="utf-8") as f:
    html = f.read()

bs = BeautifulSoup(html, "lxml") # 第二个参数是指定一个解析器

# BeautifulSoup的解析器：
# Python标准库  lxml HTML解析器  lxml XML解析器  htmlSlib
# 推荐用于lxml解析器

print(bs.prettify()) # 用更美观的形式打印出来

# 1. 获取前两个tr标签
trs = bs.find_all("tr", limit=2)    # 限制提取2个标签（返回一个列表）

# 2. 获取所有class等于even的tr标签
# 传递关键字方法
trs = bs.find_all("tr", class_="even")  # 注意class后面要加一个下划线，不然会和class冲突
# 传递字典方法：
trs = bs.find_all("tr", attrs={"class"="even"})

# 3. 将所有id等于test，class也等于test的a标签提取出来
trs = bs.find_all("a" ,attrs={"id":"test", "class"="test"})

# 4. 获取所有a标签的href属性：
hrefs = soup.find_all("a")
for href in hrefs:
    # 获取属性有2钟方式：
    # 1. 通过下标的操作的方式：
    href = a["href"]
    # 2. 通过attrs属性的方式
    href = a.attrs['href']


# 5. 获取所有的职位信息（纯文本）
trs = soup.find_all("tr")[1:]
for tr in trs:
    tds = tr.find_all("td")
    title = tds[0].string   # 这个.string方法可以把当中的字符串提取出来
    # ... 以此类推
    # 除了用.string方式来获取文本。还有另一个属性strings来更加简单的拿到标签下面所有的字符串
    # trs.strings       # 注意返回的好像是一个生成器。
