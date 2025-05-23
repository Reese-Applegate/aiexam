from django.urls import path
from django.urls import path

from . import views

urlpatterns = [
    path("", views.member_list, name="member_list"),  # "" 비어있다면, 루트 디렉토리.
    # path("<str:ids>/add/", views.member_add, name="member_add"),
    path("add/", views.member_add, name="member_add"),
    path("add/save/", views.member_add_save, name="member_add_save"),
    path("delete/<int:id>/", views.member_delete, name="member_delete"),
    path("update/<int:idx>/", views.member_update, name="member_update"),
    path("update/save/", views.member_update_save, name="member_update_save"),
    path("login/", views.login, name="login"),
    path("login/auth/", views.login_auth, name="login_auth"),
    path("logout/", views.logout, name="logout"),
]

# "" 안의 값은 url의 경로를 말한다.
# URL은 views.py의 index() 함수를 호출한다.
