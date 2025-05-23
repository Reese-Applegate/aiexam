import whisper

# large 모델 로드
model = whisper.load_model("large")

# 오디오 파일 분석
result = model.transcribe("test_korean.mp3", language="ko")  # 언어 강제 지정 가능

# 결과 출력
print(result["text"])