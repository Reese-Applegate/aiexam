import pickle

profile_file = open("profile.pkl", "wb")  # writing in binary mode.

profile = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "is_student": False,
}

print("profile:", profile)

pickle.dump(profile, profile_file)  # 덤프는 객체를 파일에 저장하는 것.
profile_file.close()  # 파일을 닫아야 함.

# 임시로 데이터를 저장하기 위한 파일을 열고, 데이터를 덤프한 후, 파일을 닫는 과정.
# 덤프한다는 것은 객체를 파일에 저장하는 것.
