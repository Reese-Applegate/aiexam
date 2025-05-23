from django.urls import path
from django.urls import path

from . import views

urlpatterns = [
    path(
        "", views.index, name="index"
    ),  # "" 비어있다면, 현재 있는 views.py에서 함수 index를 호출하라는 뜻이다.
]
# "" 안의 값은 url의 경로를 말한다.
# URL은 views.py의 index() 함수를 호출한다.
