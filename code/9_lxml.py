from lxml import etree

text = """
    <div>...
    ...这里
"""

# 将字符串解析为HTML文档
html = etree.HTML(text)  # 注意这个html现在是一个element类型的数据。

# 按字符串序列化HTML文档
# 注意解码编码。tostring返回的是byte的数据类型
result = etree.tostring(html, encoding="utf-8").decode("utf-8")
print(type(result))

def parse_text():
    htmlEle = etree.HTML(text)
    print(etree.tostring(htmlEle, encoding="utf-8"))
def parse_file():
    htmlEle = etree.parse("baidu_中国.html")
    print(etree.tostring(htmlEle, encoding="utf-8"))
if __name__ == "__main__":
    parse_file()