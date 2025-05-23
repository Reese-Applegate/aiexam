# 라이브러리 설치
from cvzone.PoseModule import PoseDetector
import cv2

cap = cv2.VideoCapture(0)

# 포즈 설정
detector = PoseDetector(
    staticMode=False,  # 정적 모드, 즉, 손이 움직이지 않는 경우. False로 설정하면 손이 움직일 때마다 손의 위치를 추적해서
    # maxHands = 2,  # 최대 손의 개수
    modelComplexity=1, # 손의 복잡성, 0이면 단순한 모델, 1이면 복잡한 모델. 1이 기본이다.
    smoothLandmarks=True, # 랜드마크를 부드럽게 하는지 여부. True로 설정하면 랜드마크를 부드럽게 한다.
    # 랜드마크를 부드럽게 하면 손의 위치가 부드럽게 움직인다. 랜드마크를 부드럽게 하지 않으면 손의 위치가 뚝뚝 끊어지면서 움직인다.
    # 랜드마크란 손의 위치를 나타내는 점이다. 손의 위치를 나타내는 점은 손가락 끝, 손목, 손바닥 등이다.
    enableSegmentation=False, # 세그멘테이션을 사용할지 여부. True로 설정하면 세그멘테이션을 사용한다.
    # 세그멘테이션이란 손의 위치를 나타내는 점을 연결해서 손의 모양을 나타내는 것이다. 세그멘테이션을 사용하지 않으면 손의 모양을 나타내지 않는다.
    smoothSegmentation=True, 
    detectionCon=0.5,
    trackCon=0.5 
)

while True:
    ret, frame = cap.read()

    img = detector.findPose (frame)
    
    cv2.imshow('pose', img)
    
    # 특정 키를 누르면 종료.
    if cv2.waitKey(1) == ord('q'):
        break

cap.release
cv2.destroyAllWindows()