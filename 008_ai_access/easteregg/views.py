from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):  # 모든 인덱스는 리퀘스트를 받아야한다.
    return HttpResponse(
        "You got me! <br> You are in the Easter Egg page. <br> This is a secret page. <br> You can find me in the Easter Egg"
    )
