import urllib3
from urllib import request, error, parse
from requests import request
from bs4 import BeautifulSoup
from requests.compat import urlparse, urljoin

seed = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=BFS&ackey=fsvikpcw"
base = urlparse(seed)[1]
tovisit = [(seed, 0)]
visited = []
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0'}
http = urllib3.PoolManager() #urllib3에서 지원
while tovisit:
    url = tovisit.pop(-1)
    resp = http.request("get", url[0], headers=headers)
    dom = BeautifulSoup(resp.data, "lxml")
    # dom = BeautifulSoup(resp.stream(), "lxml")
    visited.append(url)
    print("visited.append : ", url)
    for a in dom.select("a[href]"):
        # print("a[href] : ", a)
        new_url = urljoin(seed, a["href"])
        try:
            if not a["href"] or a["href"][0] == "#" or new_url[:4] != "http" or url[1] > 1:
                continue
        except Exception as e:
            print("error url : ", new_url)
            print("error msg : ", e)
        if new_url not in [a[0] for a in visited] + [a[0] for a in tovisit] + [seed+"/"]:
            tovisit.append((new_url, url[1] + 1))
            # print("tovisit.append : ", new_url)
    # print("tovisit size : ", len(tovisit))
print(visited)
print(len(visited))