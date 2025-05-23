import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic  # uic는 외부의 디자인 파일을 불러올때 쓴다.

form_class = uic.loadUiType("main.ui")[0]
# [0]은 모르지만 없으면 안돌아간다. 하나의 UI에 1개의 창이 존재하기 때문에 [0]을 붙인다.
# 경로가 왜이러지


class Mywindow(
    QMainWindow, form_class
):  # from_class라는 디자인을 불러온다. 편집 가능하다.
    def __init__(self):  #
        super().__init__()
        self.setupUi(self)  # setupUi는 uic에서 불러온 디자인을 적용하는 함수이다.
        self.btnlogin.clicked.connect(self.login_clicked)  # 관용어구

    def login_clicked(self):
        print("클릭!!")


app = QApplication(
    sys.argv
)  # QApplication은 PyQt5의 모든 GUI 프로그램에 반드시 필요하다. 관용어구
win = Mywindow()
win.show()
app.exec_()
