import urllib3
from urllib import request, error, parse
from requests import request
from bs4 import BeautifulSoup
from requests.compat import urlparse, urljoin
url = "https://news.daum.net"
resp = request("get", url)
dom = BeautifulSoup(resp.content, "lxml")
category = ["홈", "기후/환경", "사회", "경제", "정치", "국제", "문화", "생활", "IT/과학"]
# print([(a.txt, urljoin(resp.url, a['href'])) for a in dom.select("ul.gnb_comm > li > a[href]")
# for a in dom.select("div.flicking-panel > a[href]"):
#     print(a.contents[1].getText())
#     print(urljoin(resp.url, a['href']))
print([(a.contents[1].getText(), urljoin(resp.url, a['href'])) for a in dom.select("div.flicking-panel > a[href]")
       if a.contents[1].getText() in category])
