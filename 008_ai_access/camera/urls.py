from django.urls import path
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("video_feed", views.video_feed, name="video_feed"),
]
# "" 안의 값은 url의 경로를 말한다.
# URL은 views.py의 index() 함수를 호출한다.
