from lxml import etree
# 1. 获取所有tr标签

# 2. 获取第二个tr标签

# 3. 获取所有class等于even的标签

# 4. 获取所有a标签的href属性

# 5. 获取所有的职位信息（纯文本）

parser = etree.HTMLParser(encoding='utf-8')
html = etree.parse("tencent.html", parser=parser)

# 1. 获取所有tr标签
# //tr
trs = html.xpath("//tr")
for tr in trs:
    print(tr)


# 2. 获取第二个tr标签
# 一定要注意，xpath返回的是一个list，所以后面还要加一个[0]把值抽出来
trs = html.xpath("//tr[2]")[0]

# 3. 获取所有class等于even的标签
trs = html.xpath("//tr[@class='even']")
for tr in trs:
    print(etree.tostring(tr, encoding="utf-8").decode("utf-8"))
    # 注意要tostring，因为返回的列表是一个element。而且注意要编码解码

# 4. 获取所有a标签的href属性
# 注意，下面一行的写法是不对的。下面一行的写法是搞出所有带有href属性的a标签。如果要获取所有a标签的href属性的值！，则要：
# as = html.xpath("//a[@href]")
as = html.xpath("//a/@href")

# 5. 获取所有的职位信息（纯文本）
trs = html.xpath("//tr[position()>1]")
for tr in trs:
    # href = tr.xpath("a") # 这样会获取到一个空的列表，这样写是错误的
    # href = tr.xpath("//a", ) # 这样也是错的，写//会直接忽视tr，会在整个文档下找所有的a标签
    href = tr.xpath(".//a/@href") 
    fullurl = "http://hr.tencent.com/" + href[0]
    # 前面加一个点，表示只再tr这个标签下面找a
    # 在某个标签下，再执行xpath函数，获取这个标签下的子孙元素
    # 那么应该在//之前加一个“.”
    title = tr.xpath("./td[1]/text()")[0] # 注意这个td[1]和 /text() 函数
    category = tr.xpath("./td[2]/text()")
    # 以此类推
