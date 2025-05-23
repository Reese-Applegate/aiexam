from cafe_lib import Cafe

# def test(self):
#     print("테스트")
# def all(self):
#     print("모두")
#     self.ordering()
#     self.test()

# noBrand = Cafe()
# noBrand.ordering()
# print(type(noBrand))
# noBrand.all()

Starbucks = Cafe("스타벅스")
Twosome = Cafe("투썸플레이스")
Ediya = Cafe("이디야")

Starbucks.ordering("카페라떼", "톨", 5000)
Twosome.ordering("아메리카노", "레귤러", 4000)
Ediya.ordering("바닐라라떼", "벤티", 3000)

while True:
    sel_cafe = input("1. 스타벅스, 2. 투썸플레이스, 3. 이디야, 4. 종료) : ")

    if sel_cafe == "4":
        print("프로그램을 종료합니다.")
        break

    sel_cup_size = input("컵사이즈를 선택하세요 (톨, 레귤러, 벤티) : ")
    sel_menu = input("메뉴를 선택하세요 (아메리카노, 카페라떼, 바닐라라떼) : ")
    sel_pay = int(input("결제금액을 입력하세요 : "))
    if sel_cafe == "1":
        Starbucks.ordering(sel_menu, sel_cup_size, sel_pay)
        Starbucks.today_info()
    elif sel_cafe == "2":
        Twosome.ordering(sel_menu, sel_cup_size, sel_pay)
        Twosome.today_info()
    elif sel_cafe == "3":
        Ediya.ordering(sel_menu, sel_cup_size, sel_pay)
        Ediya.today_info()

    else:
        print("잘못된 입력입니다.")


# 노브랜드라는 변수는 클래스를 지칭한다.
# 클래스는 구조일뿐이고, 변수를 받아서, type class의 변수를 받아서 실행해야.
