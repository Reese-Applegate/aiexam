import datetime

# 오늘 날짜 구하기
now = datetime.datetime.now()
print("오늘 날짜:", now)

print(now.strftime("%Y년-%m월-%d일 %H시:%M분:%S초"))
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # 2023-10-05 14:30:00
# now는 현재 시각에 대한 정보이며, 이를 가공하여 원하는 형식으로 출력할 수 있다.
