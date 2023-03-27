# chat/views.py
from django.shortcuts import render, redirect
from accounts.models import User
import datetime
def index(request):
    return render(request, "chat/index.html")

def room(request, room_name):
    if request.user.is_authenticated:
        user = User.objects.get(pk = request.user.pk)
        x = datetime.datetime.now()
        plus = datetime.timedelta(hours=9)
        date = x + plus
        date = str(date.strftime("%m월 %d일 %H:%M"))
        context = {
            "username": user.username,
            "date": date,
            "user_pk": user.pk,
        }
        return render(request, "chat/room.html", {"room_name": room_name, "context": context})
    else:
        return redirect(request.GET.get("next") or "accounts:login")