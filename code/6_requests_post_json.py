import requests

headers = {
    'reference':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
}
data = {
    'first':True,
    'pn':1,
    'kd':'python'
}
url = "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="

response = requests.post(url=url, data=data, headers=headers)
print(type(response.text))
print("\n====================\n")
print(type(response.content))
print("\n====================\n")
# print(type(response.json())) # 如果是json的话
