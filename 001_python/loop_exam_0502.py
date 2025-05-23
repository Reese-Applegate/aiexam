# while loop 연습
cnt = 5

while cnt >= 1:
    loopcnt = 6 - cnt
    print(f"{loopcnt}번째 Loop")
    print(f"현재 카운트 : {cnt}")
    print("Hello World")
    cnt -= 1  # cnt = cnt - 1
    print(f"차감된 카운트 : {cnt}\n")
    # 5 -> 출력1 -> 4 -> 출력2 -> 3 -> 출력3 -> 2 -> 출력4 -> 1 -> 출력5 -> 0 -> 종료
    # input() # input() : 키보드 입력을 대기하는 함수, Enter를 누르면 다음으로 진행됨
print("Loop finished")

# 변수값이 조건이 맞을때는 실행하고, 맞지 않을때 종료됨.

print("-" * 60)

# for loop 연습
# range는 5미만, 미기입(시작)은 0.
for i in range(5):
    print("cnt =", i)
    print("Hello World\n")

print("-" * 60)

a = [1, 5, 10, 15, 20]
#    0, 1,  2,  3,  4
# enumate : 보이지 않는 인덱스(순서)와 값을 동시에 가져온다.
for idx, data in enumerate(a):
    print("idx =", idx)
    print("data =", data)
    print(f"a[{idx}] =", data)
    print()

print("-" * 60)

b = ["a", "b", "c", "d", "e"]
c = [1, 2, 3, 4, 5]
for (
    b1,
    c1,
) in zip(b, c):
    print("b1 =", b1)
    print("c1 =", c1)
    print(f"{b1} + {c1} = {b1 + str(c1)}")
    print()
    # zip : 두 개의 리스트를 동시에 가져온다.
    # b1, c1 : b와 c의 각각의 인덱스에 해당하는 값이 들어감.
    # b1 + str(c1) : c1은 숫자이므로 str()로 문자로 변환하여 더함.
    # b1 + str(c1) : 문자 + 문자 = 문자
    # zip은 세 개 이상의 리스트도 가능하다.
