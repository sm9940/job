#2025061702.py
from urllib import request, error, parse
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
#conda install selenium
#selenium chromedriver download
# https://googlechromelabs.github.io/chrome-for-testing/#stable
from selenium.webdriver.common.by import By

url = "http://localhost:9090/login.html"
driver = webdriver.Chrome()
driver.get(url)
print("original data\n", driver.page_source)
# id, password, 입력할 것
a = driver.find_element(By.ID, "target") # submit 찾기
print("id=target component :", a.accessible_name)
a.click()

print("post clicked data\n", driver.page_source)
dom = BeautifulSoup(driver.page_source, "lxml")
print(dom.text)
# driver.closs()
# [실시간 : https://eiec.kdi.re.kr/policy/materialList.do
# 1. 목록 안에서 검색 : 키워드는 각각 정할 것
# 2. 목록, 글쓴 기관, 날짜를 총 20개 출력

