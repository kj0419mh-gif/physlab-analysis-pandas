## XML 파일 불러오기
from bs4 import BeautifulSoup  # (이 도구를 먼저 불러와야 합니다)

data_file = open('users.xml', 'r', encoding='utf-8-sig') # 1. xml 데이터 읽기
soup = BeautifulSoup(data_file, 'xml')                   # 2. xml 데이터 파싱하기
users = soup.select('user')                              # 3. 원하는 데이터 관련 태그 선택하기
for user in users:                                       # 4. 리스트이므로 for 문으로 아이템 추출
    print(user.text)                                     # 5. 각 아이템.text 로 원하는 데이터 출력