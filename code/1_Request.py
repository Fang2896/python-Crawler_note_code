from urllib import request, parse
import json

url = "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="

# 如果有反爬虫机制。要考虑定制一些Request请求头

headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
}
data = {
    'first':True,
    'pn':1,
    'kd':'python',
}
# 伪造请求头和数据
# 注意：这里的data要用urlencode才能传到里面去（变成unicode类型）
#   而且POSE数据需要用到bytes类型。只要再将data这个东西再次encode就行了。
req = request.Request(url, headers=headers, data=parse.urlencode(data).encode('utf-8'), method='POST')

resp = request.urlopen(req)

j_data1 = resp.read().decode('utf-8')
filename1 = 'info1.json'
filename2 = 'info2.json'
with open(filename1, 'a', encoding='utf-8') as file:
    file.write(json.dumps(j_data1))

j_data2 = parse.parse_qs(resp.read().decode('utf-8'))
with open(filename2, 'a', encoding='utf-8') as file:
    file.write(json.dumps(j_data2))