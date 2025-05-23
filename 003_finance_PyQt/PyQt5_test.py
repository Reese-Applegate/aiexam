import FinanceDataReader as fdr
import pandas as pd

# SOXL 데이터 가져오기 (최근 1개월 데이터)
df_soxl = fdr.DataReader("SOXL", "2025-04-01", "2025-05-01")  # 날짜는 필요에 따라 조정

# 'Close' 열에서 5일 이동 평균 계산
ma5 = df_soxl["Close"].rolling(window=5).mean()

# 최근 5일 이동 평균 출력
if len(ma5) >= 5:  # 데이터가 충분한지 확인
    print("SOXL 최근 5일 이동 평균:", ma5.iloc[-1])
else:
    print("데이터가 부족하여 5일 이동 평균을 계산할 수 없습니다.")
