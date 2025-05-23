import cv2
# 불러오기
image = cv2.imread('./cup.jpg')
print("imaege type : ", type(image))
# 이미지 표시
cv2.imshow('cup image', image)
# Gray 이미지로 표시.
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) ##Y BGR=RGB, 순서가 다르다.
cv2.imshow('cup gray image', gray_image)
# 키 입력시까지 대기
cv2.waitKey(0)
# 종료한다.
cv2.destroyAllWindows() ##Y 리소스를 음 