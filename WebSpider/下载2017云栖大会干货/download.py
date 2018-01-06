#date   2018.1.4
#author     chenzuobao
#干货资料URL    http://click.aliyun.com/m/38596/
#基于Python网络爬虫

import requests #requests下载HTML
import bs4  #bs4解析HTML

url = "http://click.aliyun.com/m/38596/"


res = requests.get(url)
noStatchSoup = bs4.BeautifulSoup(res.text, "html.parser")
urllist = []

for a in noStatchSoup.find_all(name='a'):
    if a.string == "登录":
        url_login = str(a.get('href'))  #获得登录链接
        print(a.get('href'))
        res2 = requests.get(url_login)
        print(res2.text)
        break

for a in noStatchSoup.find_all(name='a'):
    #print(str(href.get('href')))
    if str(a.get('href'))[22:30] == "download":
        with open('download_url.txt', 'at', newline='') as f:
            f.writelines(str(a.get('href')))
        urllist.append(str(a.get('href')))
        #print(a.get('href'))
print(urllist[1])

res1 = requests.get(urllist[1])
#print(res1.text)
noStatchSoup1 = bs4.BeautifulSoup(res1.text, "html.parser")

#for url in urllist:
#    html = requests.get(url)