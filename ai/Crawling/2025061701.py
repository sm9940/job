# #2025061601.py (이전 코드에 이어지는 부분)

# urllib.request, urllib.error, urllib.parse 모듈 임포트
# request: URL을 열고 데이터를 가져오는 함수 (여기서는 urllib.request.urlopen 사용)
# error: URL 요청 시 발생할 수 있는 오류 클래스
# parse: URL을 파싱하거나 구성하는 함수 (여기서는 parse.urlencode 사용)
from urllib import request, error, parse
# requests 라이브러리 임포트 (이전 코드에서 session 객체를 사용했으나, 이 부분에서는 사용하지 않음)
import requests
# session = requests.Session() # 이전 코드에서 사용된 session 객체 생성 부분 (이어서 삭제됨)

# pip install beautifulsoup4, lxml (설치 가이드 주석)
print("########### BS ##############") # BeautifulSoup 사용 시작을 알리는 구분선 출력
# BeautifulSoup 라이브러리에서 BeautifulSoup 클래스 임포트
from bs4 import BeautifulSoup

# request.urlopen을 사용하여 네이버 검색 결과 페이지에 접속
# 검색어는 "네이버카페"이며, URL 인코딩된 형태로 전달됨
resp = request.urlopen("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query="
                     "%EB%84%A4%EC%9D%B4%EB%B2%84%EC%B9%B8%ED%8E%98&ackey=4yy0coux")
# 응답받은 HTML 내용을 lxml 파서를 사용하여 BeautifulSoup 객체로 파싱
# dom 객체를 통해 HTML 구조를 탐색하고 데이터를 추출할 수 있음
dom = BeautifulSoup(resp.read(), "lxml")

# 원본 HTML 출력을 위한 주석 처리된 부분
# print("###################### begin : original ###############################")

# selecter (CSS 선택자 사용)
# id가 "content"인 태그의 바로 아래 자식인 모든 <div> 태그를 선택하여 datas 리스트에 저장
# 스크린샷의 HTML 구조상 content 내부에는 <div class="pack_group">, <div id="sub_pack"> 등이 있을 것으로 예상
datas = dom.select('#content > div') # length = 3 -> content 바로 아래 div가 3개 있다고 가정
print(f"datas (content > div) 갯수: {len(datas)}") # 찾은 div 태그의 개수 출력

# datas 리스트의 각 인덱스에 대해 반복 (0, 1, 2)
for n in range(len(datas)):
    # #content > div:nth-of-type(n+1) CSS 선택자를 사용하여
    # id가 "content"인 태그의 바로 아래 자식 <div> 중 n+1번째 <div>를 정확히 하나 선택 (select_one)
    div = dom.select_one("#content > div:nth-of-type({})".format((n+1))) # n이 0일 때 1번째, 1일 때 2번째, 2일 때 3번째 div 선택
    
    # 선택된 div 태그의 이름, class 속성, 텍스트를 출력
    print({"tag" : div.name, "class":div['class'], "text":div.text})
    
    # datas 리스트에서 n번째 div의 class 속성을 사용하여 동일한 정보 출력
    # (위의 div와 같은 정보를 다른 방식으로 접근하여 출력하는 것을 보여줌)
    print({"tag" : div.name, "class":datas[n]["class"], "text":div.text})

print("\n########### find_previous_sibling ##############") # find_previous_sibling 메서드 사용을 알리는 구분선 출력

# datas 리스트의 두 번째 요소부터 마지막 요소까지 반복 (인덱스 1부터 시작, 즉 두 번째 div부터)
# range(1, len(datas))는 datas가 3개일 경우 n이 1, 2가 됨
for n in range(1, len(datas)):
    # id가 "content"인 태그의 바로 아래 자식 <div> 중 n번째 <div>를 선택
    # (여기서 n은 1, 2가 되므로 실제로는 2번째, 3번째 div를 선택하게 됨)
    div = dom.select_one("#content > div:nth-of-type({})".format(n))
    
    # 선택된 div 태그의 바로 이전 형제(sibling) 태그를 찾음
    # 예시: 만약 div가 <div id="main_pack">이라면, pre는 그 앞에 있는 <h1> 태그가 될 가능성이 높음
    pre = div.find_previous_sibling()
    
    # 찾은 이전 형제 태그의 이름, class 속성, 텍스트를 출력
    # 주석에 'main_pack 이전 태그 <h1>'라고 되어 있는 것을 보니, 이전 형제가 <h1> 태그일 것으로 예상
    print({"tag": pre.name, "class": pre['class'], "text": pre.text})
    
    # 현재 선택된 div 태그의 이름, class 속성, 텍스트를 출력 (두 줄 띄움)
    print({"tag": div.name, "class": div["class"], "text": div.text}, end="\n\n")

# find_previous_sibling2 (CSS 선택자와 함께 이전 형제 태그를 찾는 시도)를 위한 주석 처리된 부분
# 이 부분은 주석 처리되어 있으며, div.main_pack 선택자에 대한 추가적인 로직을 포함했었음
# print("########### find_previous_sibling2 ##############")
# for n in range(1, len(datas)):
#     # id가 "content"인 태그의 n번째 div 이후에 나오는 div.main_pack 형제 태그를 선택
#     div = dom.select_one("#content > div:nth-of-type({}) ~ div.main_pack ".format(n))
#     if (div != None) and (len(div) > 0): # div가 존재하고 길이가 0보다 클 경우
#         pre = div[0].find_previous_sibling() # 첫 번째 요소의 이전 형제를 찾음
#         print(len(div), {"tag": pre.name, "class": pre['class'], "text": pre.text}) # 이전 형제 정보 출력

print("########### ajax test ##############") # AJAX 테스트를 알리는 구분선 출력

# AJAX 요청을 보낼 로컬 서버 URL 설정
# localhost:9090/enc3.jsp는 웹 서버가 구동 중일 때 접근 가능한 로컬 경로
# parse.urlencode({'name':"홍길동"})를 사용하여 쿼리 스트링을 인코딩하고 URL에 추가
# 결과적으로 http://localhost:9090/enc3.jsp?name=%ED%99%8D%EA%B8%B8%EB%8F%99 와 같은 URL이 됨
url = "http://localhost:9090/enc3.jsp?" + parse.urlencode({'name':"홍길동"})

# 구성된 URL로 요청을 보내고 응답을 받음
resp = request.urlopen(url)

# 응답 내용을 UTF-8로 디코딩하여 data 변수에 저장
# 이 응답은 웹 서버(예: 톰캣)에서 enc3.jsp가 처리한 결과일 것으로 예상
data = resp.read().decode("utf-8")

# 디코딩된 응답 데이터(AJAX 통신 결과)를 출력
print(data)