# chat/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.models import *
import datetime

def index(request):
    return render(request, "chat/index.html")

#@login_required
#def room(request, room_name):
#    user = request.user
#    if user.is_authenticated:
#        x = datetime.datetime.now()
#        plus = datetime.timedelta(hours=9)
#        date = x + plus
#        date = str(date.strftime("%m월 %d일 %H:%M"))
#        context = {
#            "username": user.username,
#            "date": date,
#            "user_pk": user.pk,
#        }
#        return render(request, "chat/room.html", {"room_name": room_name, "context": context})
#    else:
#        return redirect(request.GET.get("next") or "accounts:login")

@login_required
def room(request, room_name):
    user = request.user
    block = []
    blocks = user.block.all()

    for i in blocks:
        block.append(i.username)
    # 로그인 검증 및 스터디원 여부 파악
    if user.is_authenticated:
        nickname = user.username
        memberimg = 'https://dummyimage.com/150x150'
    else:
        messages.error(request, "로그인을 해주세요.")
        return redirect("accounts:login")

    context = {
        "nickname": nickname,
        "memberimg": memberimg,
    }

    return render(request, "chat/room.html", {"room_name": room_name, "context": context, "block":block,})