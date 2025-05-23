def login():
    id = input("아이디 : ")
    pw = input("비밀번호 : ")

    if id == "admin":
        return True
    else:
        return False


loginCheck = login()
if loginCheck == True:
    print("로그인 성공")
else:
    print("로그인 실패")
