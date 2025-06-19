from urllib import request, error, parse
from requests import request
from bs4 import BeautifulSoup
from requests.compat import urlparse, urljoin

seed = "https://search.naver.com/search.naver?" \
       "where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=BFS&ackey=fsvikpcw"
base = urlparse(seed)[1]
tovisit = [seed]
visited = []
while tovisit:
    url = tovisit.pop(-1)
    resp = request("get", url)
    dom = BeautifulSoup(resp.content, "lxml")
    visited.append(url)
    # print("visited.append : ", url)
    for a in dom.select("a[href]"):
        # print("a[href] : ", a)
        new_url = urljoin(seed, a["href"])
        try:
            if (a["href"][0] == "#") or (urlparse(new_url)[1] != base):
                continue
        except Exception as e:
            print("error url : ", new_url)
            print("error msg : ", e)
        if new_url not in visited + tovisit + [seed+"/"]:
            tovisit.append(new_url)
            # print("tovisit.append : ", new_url)
    # print("tovisit size : ", len(tovisit))
print(visited)
print(len(visited))