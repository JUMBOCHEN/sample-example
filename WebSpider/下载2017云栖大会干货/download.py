#date   2018.1.4
#author     chenzuobao
#干货资料URL    http://click.aliyun.com/m/38596/

import requests #requests下载HTML
import bs4  #bs4解析HTML

url = "https://yq.aliyun.com/download/2305"
res = requests.get(url)
print(res.text)
noStatchSoup = bs4.BeautifulSoup(res.text)
#downloadUrl = noStatchSoup.find(class_="btn-load")
#print(downloadUrl)