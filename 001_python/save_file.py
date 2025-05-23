# 파일 입출력

saveFile = open("saveData.txt", "w", encoding="utf-8")
# 데이터를 기록한다. w는 write의 약자, 기록한다는 의미
saveFile.write("데이터 저장 파일입니다1.\n")
saveFile.write("데이터 저장 파일입니다2.\n")
saveFile.write("데이터 저장 파일입니다3.\n")
saveFile.close()  # 파일을 닫는다.
# 파일을 닫지 않으면 데이터가 저장되지 않는다.
