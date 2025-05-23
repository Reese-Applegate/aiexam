import datetime
import time

from lib.navercrawl_lib import search_naver_kin
from lib.navercrawl_lib import gen_filename
from lib.wordcloud_lib import WordCloud_Create

search = input(" 키워드 : ")
search_naver_kin(
    search
)  # 검색어를 입력받고, 해당 검색어로 네이버 지식인에서 검색하여 결과를 CSV 파일로 저장하는 함수 호출.

# filename = gen_filename(search) # 날짜와 검색어를 기반으로 파일명을 생성하는 함수 호출.
WordCloud_Create(
    f"./data/{date_time}_{time_part}_{search}.csv"
)  # 저장된 CSV 파일을 기반으로 워드클라우드를 생성하는 함수 호출.
