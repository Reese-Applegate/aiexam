<<<<<<< HEAD
# 관습적인 순서
# 1. 파이썬에서 제공되는 라이브러리
import sys
import datetime

# 2. PyQt5 라이브러리
from PyQt5.QtWidgets import *
from PyQt5.QtCore import * # QTimer는 PyQt5에서 제공하는 타이머 클래스이다.
from PyQt5 import uic # uic는 외부의 디자인 파일을 불러올때 쓴다.

# 3. 금융처리 라이브러리
import FinanceDataReader as fdr

# 라이브러리는 위에 모아둔다.

try : 
    form = uic.loadUiType("finance_main.ui")[0]
except : # 예외처리
    print("UI 파일을 찾을 수 없습니다.")
    sys.exit(1)
# UI 파일을 불러온다.

form_class = uic.loadUiType("finance_main.ui")[0] 
# [0]은 모르지만 없으면 안돌아간다. 하나의 UI에 1개의 창이 존재하기 때문에 [0]을 붙인다.
# 경로가 왜이러지

# 전역 변수
tickers = ['SOXL', 'TQQQ', 'SPXL', 'SQQQ', 'UVXY']

# 현재 값 가져오기 ( 숫자에, 넣은 값을 리턴)
def get_current_price(df_data):
    fClose = round(df_data[-1:]['Close'].values[0],2) # 소수점 2자리까지 반올림한다.
    return format(fClose, ',') # 천단위 구분기호를 넣는다.

# 5일 평균, 상승, 하락 함수

def get_5day_avg(df_data):
    # 5일 평균 구하기
    ma5 = df_data['Close'].rolling(window=5).mean() # 5일 평균을 구한다.
    fDay5 = round(ma5[-2], 2) # 소수점 2자리까지 반올림한다.

    today_data = df_data[-1:]['Close'].values[0] # 오늘의 주가를 가져온다.

    if today_data < fDay5:
        updown = "하락"
    else:
        updown = "상승"

    return format(fDay5, ','), updown
    


class Mywindow(QMainWindow, form_class): # from_class라는 디자인을 불러온다. 편집 가능하다.
    def __init__(self): # 
        super().__init__()
        self.setupUi(self) # setupUi는 uic에서 불러온 디자인을 적용하는 함수이다.
        self.btnClose.clicked.connect(self.close_clicked) # 관용어구
        self.get_stock_data() # 주식정보를 불러오는 함수를 호출한다.
        # 셀의 값 변경.

        # 타임함수 설정
        timer = QTimer(self)
        timer.start(5000) # 단위는 밀리세컨드이다. 1000ms = 1초
        timer.timeout.connect(self.timer_show)

    def timer_show(self):
        self.get_stock_data() # 주식정보를 불러오는 함수를 호출한다.

    # 주식정보 불러오는 함수
    def get_stock_data(self):
        for idx, ticker in enumerate(tickers):
            self.tblFinance.setItem((idx), 0, QTableWidgetItem(ticker))
            df_ticker = fdr.DataReader(ticker, '2025-01-01') 
            self.tblFinance.setItem((idx), 1, QTableWidgetItem(get_current_price(df_ticker)))
            day5, updown = get_5day_avg(df_ticker) # 5일 평균과 상승/하락을 가져온다.
            self.tblFinance.setItem((idx), 2, QTableWidgetItem( str(day5) ))
            self.tblFinance.setItem((idx), 3, QTableWidgetItem(updown))

        # 오늘 날짜 구하기
        now = datetime.datetime.now()
        self.lb_date.setText('갱신일자 : ' + now.strftime("%Y년 %m월 %d일 %H:%M:%S")) # setText는 텍스트를 설정하는 함수이다.
            
    def close_clicked(self):
        # print("사용자가 감히 종료를 시도함.")
        BtnResult = QMessageBox.question(
            self, '종료 확인', "정말 종료하시겠습니까?", 
            QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes
            ) # Yes, no 버튼을 만들고, 기본값은 No로 설정한다.
        if BtnResult == QMessageBox.Yes:
            # print('종료.')
            self.close() # 버튼 눌렀을때의 동작을 정의한다.
        else:
            pass
        # sys.exit() # 프로그램을 종료한다.



app = QApplication(sys.argv) # QApplication은 PyQt5의 모든 GUI 프로그램에 반드시 필요하다. 관용어구
win = Mywindow()
win.show()
app.exec_()
=======
import FinanceDataReader as fdr

df_krx = fdr.StockListing('KRX')
print(df_krx)

df_nasdaq = fdr.StockListing('NASDAQ')
print(df_nasdaq)
print 

# 주식 싫어

df_samsung = fdr.DataReader('005930', '2025-01-01', '2025-05-07')
print(df_samsung)
>>>>>>> 5b757e8bb2452ee9e98d87927cbad7b44a2eec4a
