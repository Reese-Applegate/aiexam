def userCard(
    name, phone, age=10, email=""
):  # =""는 기본옵션, 기본값이 있는 변수들은 뒤에 위치해야 한다.
    print(f"이름: {name}")
    print(f"나이: {age}")
    print(f"전화번호: {phone}")
    print(f"이메일: {email}")
    print("-" * 60)
    print(f"이름: {name}, 나이: {age}, 전화번호: {phone}, 이메일: {email}")
    print("-" * 60)
    return name, age, phone, email  # return은 여러개를 반환할 수 있다.


# userCard("홍길동", "010-1234-5678", email="raraaad")
# userCard(name="홍길동", phone="010-1234-5678", age=12, email="jinininiijini")

# hongCard = userCard("홍길동", "010-1234-5678")
# print(hongCard)

hName, hAge, _, hEmail = userCard(
    name="홍길동", phone="010-1234-5678", age=12, email="kendrick@larmar.drake"
)
# hypen변수는 값은 받는데, 사용하진 않는다. (convention)
# 많이 보던, 있어보이는 스타일
print(hName, hAge, hEmail, _)  #
