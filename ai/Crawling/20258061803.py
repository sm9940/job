from urllib import request, error, parse
# requests.compat 보다는 urllib.parse를 직접 사용하는 것이 더 명확하고 표준적입니다.
from urllib.parse import urlparse, urljoin

from requests import request as req_get # requests의 request 함수와 urllib의 request 함수 이름 충돌 방지
                                       # requests의 request 함수를 req_get으로 별칭 지정

from bs4 import BeautifulSoup
import time # 요청 간 지연 시간을 위한 time 모듈 임포트
import requests.exceptions # requests 라이브러리 예외 처리 모듈 임포트

seed = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=BFS&ackey=fsvikpcw"
base = urlparse(seed).netloc
tovisit = [seed]
visited = []
enabled = ["search", "v2"]

session = requests.Session() # requests.Session 객체 생성
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
    # 실제 브라우저 User-Agent로 변경하는 것이 좋습니다.
    # Chrome 개발자 도구 (F12) -> Network 탭 -> 아무 요청이나 클릭 -> Headers 탭 -> User-Agent 확인
}

# --- 이 부분은 삭제해야 합니다. 'url' 변수가 아직 정의되지 않았습니다. ---
# resp = session.get(url)
# ---------------------------------------------------------------------

while tovisit:
    url = tovisit.pop(0)
    
    if url in visited:
        continue # 이미 방문한 URL이면 건너뜀

    try:
        print(f"Visiting: {url}") # 현재 방문하는 URL을 출력하여 진행 상황 확인
        
        # requests.Session 객체를 사용하여 GET 요청을 보낼 때, headers를 적용합니다.
        # timeout 설정으로 무한 대기 방지 및 ConnectionResetError 완화
        resp = session.get(url, headers=headers, timeout=10) 
        
        if resp.status_code != 200:
            print(f"Error: Non-200 status code {resp.status_code} for URL: {url}")
            continue
        
        dom = BeautifulSoup(resp.content, "lxml")
        
    except requests.exceptions.RequestException as e: # requests 라이브러리 관련 모든 네트워크 오류 처리
        print(f"Network or request error for URL {url}: {e}")
        continue
    except Exception as e: # 그 외 예상치 못한 다른 오류 처리
        print(f"An unexpected error occurred for URL {url}: {e}")
        continue

    visited.append(url) # 정상적으로 처리된 URL만 visited에 추가

    for a in dom.select("a[href]"):
        href_value = a.get("href") # .get() 사용으로 KeyError 방지 (href 속성 없을 때 None 반환)

        if not href_value: # href 속성이 없거나 빈 문자열이면 건너뜀
            continue
        
        if href_value.startswith("#"): # 페이지 내 이동 링크 (#으로 시작하는 URL) 건너뛰기
            continue
        
        # urljoin의 첫 번째 인자는 현재 페이지의 URL (url)을 사용하는 것이 더 정확합니다.
        new_url = urljoin(url, href_value) 

        parsed_new_url = urlparse(new_url)
        
        # 현재 코드에서는 도메인 필터링이 비활성화되어 있지만,
        # 네이버 내의 다른 서비스 도메인으로 넘어가지 않도록 하려면 아래 주석을 해제하세요.
        # if parsed_new_url.netloc != base: # 다른 도메인으로의 링크는 건너뛰기
        #     continue

        # URL 경로 필터링: 'search' 또는 'v2'가 경로에 있으면 계속 진행
        # if not any(keyword in parsed_new_url.path for keyword in enabled):
        #     continue
        # 위 필터는 너무 광범위할 수 있습니다. 예를 들어, "/some/path/to/search_results"도 포함합니다.
        # 정확히 '/search'나 '/v2'라는 path segment를 찾는 것이 목적이라면 regex나 split 후 비교가 더 정확할 수 있습니다.
        # 현재는 주어진 코드의 로직을 유지합니다.

        # 중복 방문 방지: new_url이 이미 방문했거나(visited), 방문 예정이거나(tovisit),
        # 특정 필터링 규칙([seed+'1'])과 동일하면 건너뜀
        if new_url not in visited and new_url not in tovisit and new_url != seed + '1':
            tovisit.append(new_url)
    
    # 요청 간 간격을 두어 서버에 부하를 주지 않고, 봇으로 감지될 가능성을 줄입니다.
    time.sleep(1) # 1초 대기 (필요에 따라 조절)

print("\n--- Crawling Finished ---")
print(f"Total URLs visited: {len(visited)}")
# print("Visited URLs:")
# for u in visited:
#     print(u)