# #2025061601.py (파일 이름으로 추정)

# urllib.request, urllib.error, urllib.parse 모듈 임포트
# request: URL을 열고 데이터를 가져오는 함수
# error: URL 요청 시 발생할 수 있는 오류 클래스
# parse: URL을 파싱하거나 구성하는 함수
from urllib import request, error, parse

# requests 라이브러리 임포트
# HTTP 요청을 보내는 데 사용되는 강력하고 사용하기 쉬운 라이브러리
import requests

# requests.Session 객체 생성
# Session 객체를 사용하면 여러 요청 간에 쿠키, HTTP 헤더 등을 유지할 수 있음
session = requests.Session()

# 쿠키 테스트를 위한 URL 설정
url = "http://pythonscraping.com/pages/cookies/welcome.php"
# 로그인에 사용할 사용자 이름과 비밀번호 데이터 (딕셔너리 형태)
data = {'username':'test', 'password':'password'}
# session 객체를 사용하여 POST 요청을 보내고 응답을 받음
# 이 요청을 통해 서버로부터 쿠키(세션 정보)를 받을 수 있음
html = session.post(url, data)
# 응답받은 HTML 내용을 출력 (현재 주석 처리됨)
# print(html.text)

################################
# pip install beautifulsoup4, lxml (이것은 설치 가이드 주석)
print("########### BS ##############") # BeautifulSoup 사용 시작을 알리는 구분선 출력

# BeautifulSoup 라이브러리에서 BeautifulSoup 클래스 임포트
from bs4 import BeautifulSoup

# request.urlopen을 사용하여 네이버 검색 결과 페이지에 접속
# 검색어는 "네이버카페"이며, URL 인코딩된 형태로 전달됨
resp = request.urlopen("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query="
                     "%EB%84%A4%EC%9D%B4%EB%B2%84%EC%B9%B4%ED%8E%98&ackey=4yy0coux")
# 응답받은 HTML 내용을 lxml 파서를 사용하여 BeautifulSoup 객체로 파싱
# dom 객체를 통해 HTML 구조를 탐색하고 데이터를 추출할 수 있음
dom = BeautifulSoup(resp.read(), "lxml")

# 원본 HTML 출력을 위한 주석 처리된 부분
# print("###################### begin : original ###############################")
# print(dom)
# print("###################### end of original ###############################")

# HTML 문서의 특정 태그 경로를 따라 탐색하여 span 태그 추출 및 출력
# .html, .body, .a, .span은 태그 이름으로 접근하는 방식 (가장 먼저 나오는 태그)
print("dom.html.body.a.span :", dom.html.body.a.span) # html -> body -> a -> span 태그
print("dom.body.a.span :", dom.body.a.span)         # body -> a -> span 태그
print("dom.a.span :", dom.a.span)                 # a -> span 태그
print("dom.span :", dom.span)                     # HTML 문서에서 가장 먼저 나오는 span 태그
# 위에 주석으로 <a href="#topAsideButton"><span>상단영역 바로가기</span></a> 이 부분의 span 태그를 찾는 것으로 보임

# find_all("span")을 사용하여 모든 span 태그를 찾고 텍스트를 출력하는 주석 처리된 반복문
# for a in dom.find_all("span"):
#    # print({"tag": a.name, "id": a["id"], "text": a.text}) # id 속성도 함께 출력 (현재 id가 없는 span도 있어 에러 가능성)
#    print({"tag": a.name, "text": a.text})