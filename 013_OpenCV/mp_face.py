# 1. 라이브러리 불러오기
import cv2
import mediapipe as mp

# 2. mediapipe 초기화
mp_face = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

cap.set(3, 1280)  # 가로 해상도
cap.set(4, 720)  # 세로 해상도

with mp_face.FaceDetection(
    model_selection=0,
    min_detection_confidence=0.5
) as face_detection:
    while(True):
        ret, frame = cap.read()
        
        if not ret:
            print("빈 프레임을 읽었습니다.")
            exit()

        cv2.imshow('video input', frame)
   
        # 얼굴 인식
        frame.flags.writeable = False
        # frame.flags.writeable = False의 의미는 mediapipe가 이미지를 처리할 때, 이미지의 픽셀을 변경하지 않겠다는 의미
        # BGR 이미지를 RGB로 변환
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.imshow('video input', image)
        face_result = face_detection.process(image)
        # print(face_result)

        face_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # 감지된 얼굴에 사각형 그리기
        if face_result.detections:
            for detection in face_result.detections:
                print(detection)
                # 얼굴 감지 결과를 이미지에 그리기
                # mp_drawing.draw_detection(face_image, detection)은 mediapipe에서 제공하는 함수로, 얼굴 감지 결과를 이미지에 그리는 함수입니다.
                # detection은 얼굴 감지 결과를 나타내는 객체입니다.
                # 이 객체는 mediapipe에서 얼굴 감지 모델이 반환하는 결과로, 얼굴의 위치와 크기, 신뢰도 등을 포함하고 있습니다.
                # mp_drawing.draw_detection(face_image, detection)은 얼굴 감지 결과를 이미지에 그리는 함수입니다.
                mp_drawing.draw_detection(face_image, detection)

        cv2.imshow('Face Detection', face_image)

        # ESC키가 검출되면 종료
        key = cv2.waitKey(30) & 0xFF
        if key == 27:
            break

# 메모리 해제
cap.release()
cv2.destroyAllWindows()