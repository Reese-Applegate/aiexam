import re  # 정규 표현식 모듈


def is_valid_email(email):
    # 이메일 형식 정규 표현식
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if re.match(pattern, email):
        return True
    else:
        return False


# 이메일 입력
email = input("이메일을 입력하세요. : ")

# 이메일 형식 검사
if is_valid_email(email):
    print("유효한 이메일 형식입니다.")
else:
    print("잘못된 이메일 형식입니다.")

# 다양한 표현식에 대하여 쓸 수 있다.


def is_valid_phone(phone):
    # 전화번호 형식 정규 표현식
    pattern = r"^\d{3}-\d{3,4}-\d{4}$"

    if re.match(pattern, phone):
        return True
    else:
        return False


telno = input("전화번호를 입력하세요. : ")

if is_valid_phone(telno):
    print("유효한 전화번호 형식입니다.")
else:
    print("잘못된 전화번호 형식입니다.")
