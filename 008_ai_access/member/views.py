from datetime import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import auth


from api.models import Members


# 장고 IP 주소 가져오기
# https://www.crypist.com/post/django/views/get-user-ip-address/
def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


# Create your views here.
def index(request):  # 모든 인덱스는 리퀘스트를 받아야한다.
    return HttpResponse("Added successfully.")


def member_add(request):
    return render(request, "member/member_add.html")


def member_add_save(request):
    if request.method == "GET":
        return HttpResponse("정상적인 접근이 아닙니다.")
    ids = request.POST.get("ids", "")
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")
    email = request.POST.get("email", "")
    phone = request.POST.get("phone", "")

    print("ids :", ids)
    print("username :", username)
    print("password :", password)
    print("email :", email)
    print("phone :", phone)

    print("ids :", ids)

    savemember = Members()
    savemember.ids = ids
    savemember.username = username
    savemember.password = password
    savemember.email = email
    savemember.phone = phone
    savemember.cnts = 0
    savemember.first_dates = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    savemember.first_ips = get_client_ip(request)
    savemember.save()

    # 실제 SQL문 확인하기
    print(Members.objects.all().query)
    return redirect("member_list")


@login_required(login_url="/member/login/")
def member_list(request):
    # member_list.html
    # (SQL) SELECT * FROM api_members ORDER BY id DESC
    # 장고에서 데이터를 호출할 때 테이블명.objects.all()을 사용한다.
    memList = Members.objects.all().order_by("-id")
    print("SQL : ", memList.query)

    for mem in memList:
        print("ids :", mem.ids)
        print("username :", mem.username)
        print("password :", mem.password)
        print("email :", mem.email)
        print("phone :", mem.phone)
        print("cnts :", mem.cnts)
        print("first_dates :", mem.first_dates)
        print("first_ips :", mem.first_ips)

    return render(request, "member/member_list.html", {"data": memList})


def member_delete(request, id):
    # (SQL) DELETE FROM api_members WHERE id = id
    # 장고에서 데이터를 삭제할 때 테이블명.objects.filter().delete()을 사용한다.
    # get()은 1개만 가져오고, filter()는 여러개를 가져온다.
    # filter()는 조건에 맞는 모든 데이터를 가져온다.
    Members.objects.filter(id=id).delete()
    return redirect("member_list")


def member_update(request, idx):
    print("idx :", idx)
    try:
        memData = Members.objects.get(id=idx)
    except:
        return HttpResponse("보호하고 있는 개인 정보가 없습니다.")
    # print("SQL : ", memData.query)
    print("ids :", memData.ids)
    print("username :", memData.username)
    print("password :", memData.password)
    print("email :", memData.email)
    print("phone :", memData.phone)
    print("cnts :", memData.cnts)
    print("first_dates :", memData.first_dates)
    print("first_ips :", memData.first_ips)

    return render(request, "member/member_update.html", {"data": memData})


def member_update_save(request):
    if request.method == "GET":
        return HttpResponse("정상적인 접근이 아닙니다.")
    # 예외처리
    # 받야야할 데이터
    # id, password, email, phone
    id = request.POST.get("id", "")
    old_password = request.POST.get("old_password", "")
    email = request.POST.get("email", "")
    phone = request.POST.get("phone", "")

    print("id :", id)
    print("old_password :", old_password)
    print("email :", email)
    print("phone :", phone)

    try:
        memEdit = Members.objects.get(id=id, old_password=old_password)
    except:
        return HttpResponse("비밀번호가 틀립니다.")

    # 수정
    memEdit.email = email
    memEdit.phone = phone
    memEdit.save()

    return redirect("member_list")


def login(request):
    return render(request, "auth/login.html")


def logout(request):
    return render(request, "auth/logout.html")


def login_auth(request):
    if request.method == "GET":
        return HttpResponse("정상적인 접근이 아닙니다.")

    email = request.POST.get("email", "")
    password = request.POST.get("password", "")

    username = User.objects.get(email=email)

    user = authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return redirect("member_list")
    print("email :", email)
    print("password :", password)

    return HttpResponse("정상적인 접근입니다.")
