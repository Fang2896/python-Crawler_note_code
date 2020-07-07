from urllib import request
from http.cookiejar import MozillaCookieJar


# 火狐公司的cookie格式，文件名为cookie
cookiejar = MozillaCookieJar("cookie.txt")
cookiejar.load(ignore_discard=True)  # 如果有cookie则可以用load函数来进行加载.这里的ignore_discard参数也是加载过期的cookie信息。
handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)
# 这个网站真的好用
# 但这个网站cookies过期信息是所有网站会话关闭的时候就马上过期了
# 所以要传递另一个参数。ignore_discard
resp = opener.open("http://www.httpbin.org/cookies/set?course=abc")

# save方法要传递一个filename的参数，但如果MozillaCookiejar里面已经传递了。这里就用不着传递了
# cookiejar.save(ignore_discard=True)

# load函数是在制顶文件中将cookie加载进来
for cookie in cookiejar:
    print(cookie)   # 成功