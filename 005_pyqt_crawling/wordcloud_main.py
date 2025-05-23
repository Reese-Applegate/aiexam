import sys
import os

from PyQt5.QtWidgets import *
from PyQt5 import uic  # uic는 외부의 디자인 파일을 불러올때 쓴다.
from PyQt5.QtGui import *
from lib.navercrawl_lib import search_naver_kin
from lib.wordcloud_lib import WordCloud_Create

form_class = uic.loadUiType("./005_pyqt_crawling/ui/wordcloud_main.ui")[0]
# [0]은 모르지만 없으면 안돌아간다. 하나의 UI에 1개의 창이 존재하기 때문에 [0]을 붙인다.
# 경로가 왜이러지


class Mywindow(
    QMainWindow, form_class
):  # from_class라는 디자인을 불러온다. 편집 가능하다.
    def __init__(self):  #
        super().__init__()
        self.setupUi(self)  # setupUi는 uic에서 불러온 디자인을 적용하는 함수이다.
        self.setFixedSize(710, 688)  # 창 크기를 고 정 한 다 .
        self.btn_close.clicked.connect(self.close_clicked)  # 관용어구
        self.btn_close_2.clicked.connect(self.close_clicked)  # 관용어구
        self.btn_search.clicked.connect(self.search_clicked)
        self.btn_process.clicked.connect(self.process_clicked)

    def close_clicked(self):
        # print("종료버튼.")
        btn_close = QMessageBox.question(
            self,
            "종료 확인",
            "정말 종료하시겠습니까?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes,
        )  # Yes, no 버튼을 만들고, 기본값은 No로 설정한다.
        if btn_close == QMessageBox.Yes:
            # print('종료.')
            self.close()  # 버튼 눌렀을때의 동작을 정의한다.
        else:
            pass
        # sys.exit() # 프로그램을 종료한다.

    def search_clicked(self):
        # print("검색을 시도하였다.")
        search = self.ed_search.text()
        # 지역변수 : 함수안에서만 쓰인다. class에서 다 쓰이는건 전역변수다.
        if search == "":
            QMessageBox.warning(self, "검색어를 입력하세요", "검색어를 입력하세요")
            return
        save_file_qt = search_naver_kin(
            search
        )  # lib내의 return값인 save_file을 save_file_qt에 저장한다.
        self.ed_result.setText(save_file_qt)
        self.ed_file.setText(save_file_qt)  # 검색한 결과를 ed_result에 저장한다.
        self.ed_stopword.setText(search)

    def process_clicked(self):
        ed = self.ed_file.text()
        # ed_file이 비어있음
        if ed == "":
            QMessageBox.warning(self, "검색부터 하자?")
            return
        # ed_file의 파일이 존재하는지 확인
        if os.path.exists(ed) == False:
            QMessageBox.warning(self, "파일이 존재하지 않음", "파일이 존재하지 않음")
            return
        # ed_file의 확장자 확인
        extFile = os.path.splitext(ed)[1]
        if extFile != ".csv":
            QMessageBox.warning(self, "파일이 csv가 아님", "파일이 csv가 아님")
            return

        input_stopwords = self.ed_stopword.text()

        cloud_path = WordCloud_Create(ed, input_stopwords)
        self.qPixmapfileVar = QPixmap()
        self.qPixmapfileVar.load(cloud_path)
        self.qPixmapfileVar = self.qPixmapfileVar.scaled(671, 503)
        self.lb_word.setPixmap(self.qPixmapfileVar)


app = QApplication(
    sys.argv
)  # QApplication은 PyQt5의 모든 GUI 프로그램에 반드시 필요하다. 관용어구
win = Mywindow()
win.show()
app.exec_()
