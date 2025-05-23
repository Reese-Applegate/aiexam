import torch

# 모델 불러오기
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# 샘플 이미지
img = 'https://i.ytimg.com/vi/BkV4QSpVdA8/maxresdefault.jpg'
# 예측 : predict
results = model(img)

# 결과 확인
results.print() # 콘솔에 출력
results.show()  # 이미지로 출력