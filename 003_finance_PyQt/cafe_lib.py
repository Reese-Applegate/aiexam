class Cafe:
    menu = ""
    cafe_name = ""
    total_pay = 0

    def __init__(self, cafe_name):  # 시작하면서 실행. 무조건 실행.
        self.cafe_name = cafe_name

    # coffee = "아이스커피"

    def ordering(self, menu, cup_size, pay):
        self.menu = menu
        self.total_pay = self.total_pay + pay
        print(
            f"[{self.cafe_name}] 주문 : {self.menu}, 컵사이즈 : {cup_size}"
        )  # self는 인스턴스 변수를 의미한다.

    def today_info(self):
        print("=" * 40)
        print(f"[{self.cafe_name}] 오늘은 매출은 {self.total_pay}원입니다.")
        print("=" * 40)

        ##
