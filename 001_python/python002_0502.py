# 입력함수
a = input("숫자를 입력하세요 : ")
print(type(a))

if int(a) < 10:
    print(f"{a}는 10보다 작습니다.")
elif a == 10:
    print(f"{a}는 10입니다.")
else:
    print(f"{a}는 10보다 큽니다.")

print(type(int(a)))
