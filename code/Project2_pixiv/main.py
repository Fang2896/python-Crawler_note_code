import requests
from bs4 import BeautifulSoup
import re, os, requests
# from multiprocessing import Pool

# rank_url = "https://www.pixiv.net/ranking.php"
# base_url = "https://www.pixiv.net/artworks/"
# login_url = "https://accounts.pixiv.net/login"


# 参考url
# 缩略图：
# https://i.pximg.net/c/240x480/img-master/img/2019/02/24/00/00/27/73355010_p0_master1200.jpg
# 原图：
# https://i.pximg.net/img-master/img/2019/02/24/00/00/27/73355010_p0_master1200.jpg
# 考虑采用正则匹配来通过缩略图来获取原图。以避免登录

# 获取某年某月的排行榜缩略图网址，并返回列表
def geturl(year,month):
    headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "referer":"https://www.pixiv.net/ranking.php"
    }
    baseurl='https://www.pixiv.net/ranking.php?mode=monthly&content=illust&date={}{}01'.format(str(year),str(month).zfill(2))
    html=requests.get(baseurl, headers=headers)
    soup=BeautifulSoup(html.content,'lxml')
    a=soup.find_all(class_='_layout-thumbnail')
    urllist=[]
    for i in a:
        target = i.find('img').get('data-src')
        urllist.append(target)
        print(target,"\n")
        print(re.search("\d{8}", target).group())
    print("Get URL Sucecess.\n")
    return urllist

# change_url函数将缩略图网址用字符串替换方法得到原网址
def change_url(llist):
    orilist = []    # 原图网址
    for i in llist:
        tem = re.search("/c/\d{0,3}x\d{0,3}/img-master/", i).group()
        i = i.replace(tem, "/img-master/")
        orilist.append(i)
    print("Change URL Sucess.\n")
    return orilist

# download函数为下载指定图片,命名为# rank-pid
def download(url, rank, fnum):
    headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    }
    pid = re.search('\d{8}', url).group()
    headers["referer"] = 'https://www.pixiv.net/member_illust.php?mode=medium&illust_id='+pid
    
    img = requests.get(url, headers=headers).content

    with open('{}#{}-{}.jpg'.format(str(fnum), str(rank), pid), "wb") as f:
        f.write(img)
        print("Download sucecess: {}".format(rank))


if __name__=="__main__":
    os.chdir("F:\\H_img")
    # p = Pool(8)
    urls=change_url(geturl(2020, 6))
    rank = 1
    for i in urls:
        download(i, rank, 6)
        rank=rank+1
    
    # p.close()
    # p.join()
