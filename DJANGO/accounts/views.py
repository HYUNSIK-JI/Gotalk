from django.shortcuts import render, redirect
from .forms import CreateUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, login as my_login, logout as my_logout
from .forms import CreateUser
from .models import User


# Create your views here..

def signup(request):
    if request.method == "POST":
        form = CreateUser(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            my_login(request, user)
            return redirect(request, "accounts/login.html")

    else:
        form = CreateUser()
    context = {
        "form": form,
    }
    print(form.errors)

    return render(request, "accounts/signup.html", context)

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        print(1)
        if form.is_valid():
            my_login(request, form.get_user())
            return redirect(request.GET.get("next") or "accounts:signup")
        else:
            form = AuthenticationForm()
            context = {"form": form}
            return render(request, "accounts/login.html", context)
    else:
        form = AuthenticationForm()
    context = {"form": form}
    return render(request, "accounts/login.html", context)

@login_required
def logout(request):
    my_logout(request)
    return redirect("accounts:signup")

@login_required
def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    pass