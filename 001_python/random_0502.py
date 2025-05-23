from random import *  # asterisk is used to import all functions from the random module

# 별표는 random 모듈에서 모든 함수를 가져오는 데 사용됩니다.
# random.py라는 프로그램 파일에서 모든 함수를 사용하겠다.
from addlib.gugudan import *  # 내가 만든 라이브러리에서 gugudan이라는 함수를 가져올 수 있다.

# 쉽게 만들기위해 폴더를 만들고, 라이브러리로 프로그램을 쪼갠다.
# 예를 들면,

print(random())

# gugudan()
# test()

print(randrange(1, 10))  # 1~9까지의 랜덤한 숫자
print(
    f"금주의 행운 번호 : {randint(1, 45),randint(1, 45),randint(1, 45),randint(1, 45),randint(1, 45),randint(1, 45)}"
)  # 45는 포함되지 않음
print(f"{randint(1, 6)}등 번호!")

cutline = print("-" * 60)

# 형변환 연산자

a = "3.14"
fa = float(a)
print(fa)
print(type(fa))

a = "3.14"
fa = float(a)
ia = int(fa)
print(fa)
print(ia)
print(type(fa))
# 소수를 바로 정수로 정의할수없지만, 소수를 정수로 바꿔서 정의할 수 있다?
