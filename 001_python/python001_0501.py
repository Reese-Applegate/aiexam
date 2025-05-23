#########################################################################
# Python 001 - Hello World
# Author: Your Name
# Date: 2023-10-01
# Description: This script prints "Hello, World!" and demonstrates string literals.
# License: MIT License
# Version: 1.0
# Notes: This is a simple script to demonstrate basic Python syntax and string handling.
# It includes examples of single and double quotes, as well as escaping characters.
# It also includes a simple function to print the multiplication table (gugudan).
# The function is not called in this script, but it can be uncommented for use.
# Usage: Run this script in a Python environment to see the output.
# Dependencies: None
##########################################################################
print("Hello, World!")
print("Hello, World!")
print("I can't believe it's not butter!")
print(12_354_315_345 + 4_541_684_646)  # 가독성을 위해 언더바 사용
# 사칙연산
print(9 + 7)  # 덧셈
print(9 - 7)  # 뺄셈
print(9 * 7)  # 곱셈
print(9 / 7)  # 나눗셈
print(9 // 7)  # 몫
print(9 % 7)  # 나머지
# 페이징 처리 예시
print("몫 : ", 9 // 7)  # 페이지 수
print("나머지 : ", 9 % 7)  # 마지막 페이지에 남는 데이터 수
# 제곱과 제곱근
print(9**7)  # 제곱
print(9**0.5)  # 제곱근
###########################################################################
# 변수 선언 및 사용 예시
# 변수 선언
# 변수는 대입 연산자를 사용하여 값을 저장합니다.
# 변수 이름은 알파벳, 숫자, 언더바(_)로 시작할 수 있으며, 대소문자를 구분합니다.
# 변수 이름은 예약어와 중복되지 않아야 합니다.
# 예약어는 Python에서 특별한 의미를 가지는 단어로, 변수 이름으로 사용할 수 없습니다.
print("변수")  # 변수 선언 및 사용 예시
a = 5  # 정수형 변수
b = 4  # 정수형 변수
print(a + b)  # 덧셈
print(a - b)  # 뺄셈
print(a * b)  # 곱셈
# 대문자로 각 단어의 시작을 표시한다. 독일어스타일
print("#" * 40)
test_var = 5
testVar = 4
print(test_var)  # 5
print(testVar)  # 4
print(f"값은 = {testVar}")  # 엑셀스타일
# f string을 사용하여 변수 값을 문자열에 삽입할 수 있습니다.
# f string은 중괄호({})를 사용하여 변수 이름을 감싸면 됩니다.
print("#" * 40)
print(type(testVar))  # 변수의 타입을 출력합니다.
strA = "Hello"  # 문자열 변수
print(type(strA))  # 변수의 타입을 출력합니다.

# 실수
f1 = 3.456789  # 실수형 변수
print(type(f1))  # 좌표에서 자주 사용되는 실수형 변수
print(f"{f1:.2f}, {f1:.4f}")  # 소수점 둘째자리까지 출력합니다.
print(f"{f1:.3f}")  # 소수점 셋째자리까지 출력합니다.
print(
    round(f1, 2), round(f1, 3)
)  # round() 함수를 사용하여 소수점 둘째자리까지 반올림합니다.

# 퀴즈
f2 = 1
f3 = 1.0
print(f2)
print(f3)
print("#" * 40)
# 문자열의 길이를 구하는 함수
testStr = "테스트1234"
print(len(testStr))  # 문자열의 길이를 구합니다. 한글도 1글자로 계산됩니다.

# 문자열 합치기
strA = "문자열1"
strB = "문자열2"
print(strA + strB)  # 문자열을 합칩니다.
intC = 1234
# print(strA + strB + intC)
print(
    strA + strB + str(intC)
)  # 문자열과 정수를 합칩니다. 정수는 문자열로 변환하여 합칩니다.
print(f"{strA}{strB}{intC}")  # f string을 사용하여 문자열과 정수를 합칩니다.

print("#" * 40)
print("조건문")
testVar = 5
testVar2 = 4
if testVar == 5 and testVar2 == 4:
    print("testVar는 5입니다.")
    print("testVar2는 4입니다.")
else:
    print("아이디 혹은 비밀번호가 다릅니다.")

if testVar == 5:
    print("testVar는 5입니다.")
if testVar2 == 4:
    print("testVar2는 4입니다.")
else:
    print("아이디 혹은 비밀번호가 다릅니다.")

if testVar == 5:
    print("testVar는 5입니다.")
elif testVar2 == 4:
    print("testVar2는 4입니다.")
else:
    print("아이디 혹은 비밀번호가 다릅니다.")
## colon(:)을 사용하여 블록을 구분합니다.
## ==는 비교 연산자입니다.

g1 = 5
if g1 == 5:
    print("g1은 5입니다.")
else:
    print("g1은 5가 아닙니다.")

# bool형
toggle = True

if toggle:
    print("True입니다.")
else:
    print("False입니다.")
