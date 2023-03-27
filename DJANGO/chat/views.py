# chat/views.py
from django.shortcuts import render, redirect


def index(request):
    return render(request, "chat/index.html")

def room(request, room_name):
    if request.user.is_authenticated:
        return render(request, "chat/room.html", {"room_name": room_name})
    else:
        return redirect(request.GET.get("next") or "accounts:login")