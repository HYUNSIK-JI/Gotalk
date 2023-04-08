# chat/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Gotalk.settings import CACHES
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
    r = request.path
    r = r.split("/")
    rr = r[2].split("Gotalk")
    

    send = rr[0]
    receive = rr[1]

    user = request.user
    block = []
    blocks = user.block.all()

    w = CACHES.get(str(r[2]))
    check = 1
    if w:
        print(w)
        check = 0
    for i in blocks:
        block.append(i.username)
    
    if user.is_authenticated:
        nickname = user.username
        memberimg = 'https://dummyimage.com/150x150'
    else:
        messages.error(request, "로그인을 해주세요.")
        return redirect("accounts:login")

    context = {
        "nickname": nickname,
        "memberimg": memberimg,
        "w":w,
        "check":check,
    }

    return render(request, "chat/room.html", {"room_name": room_name, "context": context, "block":block,})