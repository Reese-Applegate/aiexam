import pickle

profile_file = open("profile.pkl", "rb")  # reading in binary mode.
# rb는 읽기 전용 모드로 파일을 열 때 사용.
profile = pickle.load(profile_file)  # 로드한다는 것은 파일에서 객체를 읽어오는 것.

print(profile)

profile_file.close()  # 파일을 닫아야 함.


# Pickle을 사용하는 이유 :
# 저작권 등으로 민감한 데이터를 Pickle형태로 제공해서 활용만 가능하고, 가공은 불가능하기 위해 사용.
