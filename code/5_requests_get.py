#encoding: utf-8

import requests

# response = requests.get("https://www.baidu.com/")
# print(type(response.text))
# print(response.text)  #这样会乱码，因为是gbk类型
# print("\n=========================================\n")
# print(response.content)
# print("\n=========================================\n")
# print(response.content.decode("utf-8"))
# print("\n=========================================\n")
# print(response.status_code)
# print("\n=========================================\n")
# print(response.url)
# print("\n=========================================\n")
# print(response.encoding)
# print("\n=========================================\n")

# params 测试
params = {
    "wd":"中国"
}
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}

response = requests.get("https://www.baidu.com/s", params=params, headers=headers)

with open('baidu_中国.html',"w",encoding="utf-8") as fp:
    fp.write(response.content.decode('utf-8'))
print(response.url)
# 现在百度会有安全验证

