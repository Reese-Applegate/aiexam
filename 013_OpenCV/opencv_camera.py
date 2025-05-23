import cv2
# 카메라 제어
cap = cv2.VideoCapture('./messy.mp4') ##Y 카메라에 숫자를 할당하면 카메라가 나오고, 경로를 할당하면 영상이 나온다.
# 카메라 사이즈
# (640, 480), (1280)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640) 
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
while cv2.waitKey(33) < 0: 
    # 카메라에서 이미지를 하나씩 불러옴
    _, frame = cap.read()
    # 그레이 처리
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Camera 0', frame)
    cv2.imshow('Camera 0 Gray', img_gray)
# 종료
cap.release()
cv2.destroyAllWindows()