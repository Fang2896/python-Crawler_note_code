from urllib import request

url = 'http://httpbin.org/ip'
# 用ProxyHandler传入代理构建一个handler
handler = request.ProxyHandler({"http":"27.43.190.180:9999"})
# 使用上面创建的handler构建一个opener
opener = request.build_opener(handler)

# 用opener去发送一个请求
resp = opener.open(url)
print(resp.read())



# 注： 现在貌似没用了