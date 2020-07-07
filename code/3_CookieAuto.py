from urllib import request
from urllib import parse
from http.cookiejar import CookieJar


headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
}
data = {
    'email':'18970772621',
    'password':"LIU3070FANG"
}
login_url = "http://www.renren.com/PLogin.do"


def get_opener():
    # 1. 登陆
    # 1.1 创建一个cookiejar对象
    cookiejar = CookieJar()
    # 1.2 使用cookiejar创建一个HTTPCookieProcess对象
    handler = request.HTTPCookieProcessor(cookiejar)
    # 1.3 使用上一步创建的handler创建一个opener
    opener = request.build_opener(handler)
    return opener

def login_renren(opener, login_url, headers, data):
    # 1.4 使用opener发送登陆的请求（邮箱和密码）
    req = request.Request(login_url, headers=headers, data=parse.urlencode(data).encode('utf-8'))
    opener.open(req)

def visit_profile(opener, headers):
    # 2. 访问个人主页

    dapeng_mainpage_url = "http://www.renren.com/880151247/profile"
    # 这里使用之前的opener。之前的opener已经包含了登陆所需要的信息
    req = request.Request(dapeng_mainpage_url, headers=headers)
    resp = opener.open(req)
    # 写到本地文件当中
    with open("renren_dapeng.html", "w", encoding="utf-8") as fp:
        fp.write(resp.read().decode('utf-8'))


if __name__ == '__main__':
    opener = get_opener()
    login_renren(opener, login_url, headers, data)
    visit_profile(opener,headers)
