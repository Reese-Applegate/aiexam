import FinanceDataReader as fdr

# apple = fdr.DataReader('AAPL', '2020-01-01')  # 'AAPL'은 애플의 티커 코드
# current_price = apple['Close'][-1]
# last_month_avg = apple['Close'][-30:].mean()
# price_change = current_price - last_month_avg

# print(f"현재가: {current_price}")
# print(f"최근 1달 평균: {last_month_avg}")
# print(f"현재의 상승/하락 값: {price_change}")

# df_apple = fdr.DataReader('AAPL', '2025-05-01') #뒤에 없으면 오늘까지.
# print(df_apple)  # 데이터프레임의 처음 5개 행을 출력합니다.

df_SOXL = fdr.DataReader("SOXL", "2025-05-01")  # 뒤에 없으면 오늘까지.
# print(df_SOXL)  # 데이터프레임의 처음 5개 행을 출력합니다.
print(type(df_SOXL[-1:]["Close"].values[0]))  # 얘는 numpy.float64형
print(type(round(df_SOXL[-1:]["Close"].values[0], 2)))  # 애는 실수형
print(type(f"{df_SOXL[-1:]['Close'].values[0]:,.2f}"))  # 얘는 문자열
