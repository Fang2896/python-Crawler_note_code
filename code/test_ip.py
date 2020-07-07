import requests

url_ip = "http://www.httpbin.org/ip"
url_pixiv_rank = "https://www.pixiv.net/ranking.php"
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "referer":"https://www.pixiv.net/ranking.php"
}
ip_resp = requests.get(url_ip)

# print(ip_resp.text)

p_resp = requests.get(url_pixiv_rank, headers=headers)
print(p_resp.status_code)
with open("pixiv_rank.html", "w", encoding="utf-8") as fp:
    fp.write(p_resp.content.decode("utf-8"))