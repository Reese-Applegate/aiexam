from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):  # 모든 인덱스는 리퀘스트를 받아야한다.
    # return HttpResponse(f"Landing 페이지이다. <br>member, camera, ai, api 페이지가 현재 개발중에 있다.")
    # 데이터 구조 만들기
    sendData = {
        "titles": "인공지능 출입관리 프로젝트",
        "sub_titles": "by Face Recognition, Dlib, CNN, FAISS, OpenCV",
        "state_msg": "즉시 접속",
    }
    return render(request, "landing/main.html", sendData)
