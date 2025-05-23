import cv2
# 불러오기
image = cv2.imread('./cup.jpg', cv2.IMREAD_COLOR)
print("imaege type : ", type(image))
# Gray 이미지로 표시.
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) ##Y BGR=RGB, 순서가 다르다.
# 흑백 이미지 특정 부분 자르기
cut_image = gray_image[100:500, 200:700].copy() ##Y 일반적으로 복사가 되는데, 가끔 잘라내기가 되는 [오류]가 발생하므로, 이를 막기 위하여 강제로 copy()라는 명시적 표현을 한다.
# 원본 이미지 표시
cv2.imshow('cup image', image)
cv2.imshow('cup gray image', gray_image)
cv2.imshow('cut image', cut_image)
# 이미지 저장
cv2.imwrite('./cup_gray.jpg', gray_image)
# 키 입력시까지 대기
cv2.waitKey(0)
# 종료한다.
cv2.destroyAllWindows() ##Y 리소스를 음 