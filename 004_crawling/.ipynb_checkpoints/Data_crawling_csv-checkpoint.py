import csv
import datetime
import time
import random

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus 

# 날짜로 파일명 만드는 함수
def gen_filename(search):
    current_time = datetime.datetime.now()
    date_time = current_time.strftime("%Y%m%d")
    time_part = current_time.strftime("%H%M%S")
    return f"/data/{date_time}_{time_part}_{search}.csv"

search = input("검색어를 입력하세요: ")
print("검색어: ", search)

# 저장한 파일 열기 : 파일명 
# 20250508_AI.csv
# 할때마다 자동으로. 아니면 못찾겠죠.
# 보통은 할때 
# 20250508_143507_AI.csv 시간도 써준다.
# 년월일_시분초_검색어.csv got it.
save_file = gen_filename(search)
print("저장할 파일명: ", save_file)
f = open(save_file, 'w', encoding='cp949', newline='') # 엑셀파일은 encding=cp949 for preventing broken korean.
csvWriter = csv.writer(f) # csv writer 객체, csv방식으로 저장하라. 


# Paging
for i in range (0): # 100은 천개. 하나랑 10개의 데이터가 있었어.

    # 검색을 위한 quote_plus 인코딩 작업
    url = f"https://kin.naver.com/search/list.naver?query={quote_plus(search)}&page={i+1}"
    print("url: ", url)

    # 정보 가져오기
    html = urlopen(url).read()
    print("html: ", html)

    # BeautifulSoup 으로 html 파씽
    soup = bs(html, "html.parser")
    total = soup.select('.basic1 > li > dl > dt > a') # html 페이지 소스에서 원하는 부분을 parsing.
    print("total = ", len(total))

    # 해당부분 출력
    for idx, data in enumerate(total):
        print("#" * 20 + str(idx + 1) + "#" * 20)
        print(data)

        # 제목만 검출  
        title = data.text
        print("title: ", title) # 텍스트만.

        # 링크만 검출
        link = data.attrs['href']
        print("link: ", link) # 링크만.

        csvWriter.writerow([title, link]) # csv파일에 제목과 링크를 저장한다.

    delay_time = random.randint(1, 10)
    time.sleep(delay_time) # 랜덤으로 1초에서 10초 사이의 시간동안 대기한다.

f.close() # 파일을 닫는다.
# 파일을 닫지 않으면 데이터가 저장되지 않는다.