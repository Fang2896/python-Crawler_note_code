from bs4 import BeautifulSoup

# "..."


soup = BeautifulSoup(html, 'lxml')

# 1. 获取所有的tr标签
trs = soup.select("tr")     # 返回的也是tag类型

# 2. 获取第二个tr标签
tr2 = soup.select("tr")[1]

# 3. 获取所有class等于even的tr标签
trs = soup.selecty("tr.even")
# 或者：
trs = soup.select("tr[class='evev']")

# 4. 获取所有的a标签的href属性
aList = soup.select("a")
for i in aList:
    infos = list(tr.stripped_strings)

# 5. 获取所有的职位信息：

