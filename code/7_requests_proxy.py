import requests
proxy = {
    'https':'183.166.96.149:9999'
}

response = requests.get("http://www.httpbin.org/ip",proxies=proxy)
print(response.text)