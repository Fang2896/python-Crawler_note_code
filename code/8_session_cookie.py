import requests

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
}
data = {
    'email':'18970772621',
    'password':"LIU3070FANG"
}
login_url = "http://www.renren.com/PLogin.do"


response = requests.get("https://www.baidu.com/")

print(response.cookies,'\n')
print(response.cookies.get_dict())

# 创建session对象
session = requests.Session()

session.post(login_url, data=data,headers=headers)

# 看看能不能访问到主页：
response = session.get("http://www.renren.com/880151247/profile")

with open("session_test_renren.html", "w", encoding="utf-8") as fp:
    fp.write(response.text)
