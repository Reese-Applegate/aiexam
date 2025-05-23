import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):  # QMainWindow는 PyQt5에서 제공하는 기본 창이다.
    def __init__(self):  # 생성자
        super().__init__()
        self.setGeometry(
            200, 300, 640, 480
        )  # Set the window size and position (x, y, width, height)
        self.setWindowTitle("PyQt5 Window")  # 이름바꾸기
        # 위에 네줄도 그냥 관용어구.
        # 클래스는 다음주에 자세하게..
        btn = QPushButton("버튼 클릭", self)
        btn.move(100, 100)
        btn.clicked.connect(
            self.button_clicked
        )  # 버튼 클릭 시 button_clicked 메소드 호출

    def button_clicked(self):  # 버튼 클릭 시 호출되는 메소드
        print("버튼이 클릭되었습니다.")  # 버튼 클릭시 작동


# Self는

app = QApplication(sys.argv)

win = MyWindow()  # Create an instance of the MyWindow class
win.show()

# label = QLabel("안녕 PyQt5!") # Label은 글자다.
# label.show()# Show the label
# btn = QPushButton("버튼이네.") # Button은 버튼이다.
# btn.show() # Show the button


app.exec_()  # Excute the application

# Python(PyQt5)는 다양한 OS에서도 동일하게 동작한다는 장점이 있다.
# 단, Mobile 환경에서는 지원하지 않는다.
# 무료 이용에는 자유롭지만, 상업적 이용은 라이센스 구매가 필요하다.
