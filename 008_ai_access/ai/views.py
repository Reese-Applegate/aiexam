from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):  # 모든 인덱스는 리퀘스트를 받아야한다.
    return HttpResponse("Am I AI?")
