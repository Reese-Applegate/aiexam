# 라이브러리 설치
from cvzone.HandTrackingModule import HandDetector
import cv2

cap = cv2.VideoCapture(0)

detector = HandDetector(
    staticMode=False,  # 정적 모드, 즉, 손이 움직이지 않는 경우. False로 설정하면 손이 움직일 때마다 손의 위치를 추적해서
    # 손의 위치를 업데이트합니다.
    # staticMode=True로 설정하면 손이 움직이지 않는 경우에도 손의 위치를 업데이트합니다.
    # staticMode=False로 설정하면 손이 움직일 때마다 손의 위치를 업데이트합니다.
    maxHands = 2,  # 최대 손의 개수
    modelComplexity=1, # 손의 복잡성, 0이면 단순한 모델, 1이면 복잡한 모델. 1이 기본이다.
    detectionCon=0.5,  # 손을 감지하는 신뢰도, 0.5이면 50%의 신뢰도로 손을 감지한다. 
    minTrackCon=0.5  # 손을 추적하는 신뢰도, 0.5이면 50%의 신뢰도로 손을 추적한다.
    # 추적과 감지의 차이는 손을 감지하는 것과 손을 추적하는 것이다. 감지는 손이 있는지 없는지를 판단하는 것이고, 추적은 손이 어디에 있는지를 판단하는 것이다.
)




while True:
    ret, frame = cap.read()

    hands, img = detector.findHands(frame, draw=True, flipType=True)
    
    # 오른손 왼손 체크
    if hands:
        for hand in hands:
            print(hand['type'])

    cv2.imshow('hand view', img)

    # 특정 키를 누르면 종료.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break