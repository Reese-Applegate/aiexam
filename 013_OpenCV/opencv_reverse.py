import cv2
# 불러오기
image = cv2.imread('./cup.jpg', cv2.IMREAD_COLOR)
# 대칭
rev_image = cv2.flip(image,0) # 0: 수직 대칭, 1: 수평 대칭, -1: 수직+수평 대칭
# 원본 이미지 표시
cv2.imshow('cup image', image)
cv2.imshow('cup reverse image', rev_image)
# 키 입력시까지 대기
cv2.waitKey(0)
# 종료한다.
cv2.destroyAllWindows() ##Y 리소스를 음 