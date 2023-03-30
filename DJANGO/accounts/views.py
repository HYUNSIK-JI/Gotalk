from django.shortcuts import render, redirect
from .forms import CreateUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, login as my_login, logout as my_logout
from django.http import JsonResponse
from .forms import CreateUser
from .models import User


# Create your views here..

def index(request):
    users = User.objects.all()
    context  = {
        "users": users,
    }
    return render(request, "accounts/main.html", context)

def signup(request):
    if request.method == "POST":
        form = CreateUser(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            my_login(request, user)
            return redirect(reverse('login'))

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
    context = {
        "user": user,
        "block_system": user.block_system.all(),
        "block": user.block.all(),
    }
    return render(request, "accounts/detail.html", context)


@login_required
def block(request, pk):
    if request.user.is_authenticated:
        user = User.objects.get(pk=pk)
        if user != request.user:
            if user.block_system.filter(pk=request.user.pk).exists():
                user.block_system.remove(request.user)
                is_block = False
            else:
                user.block_system.add(request.user)
                is_block = True
            
            blocks = user.block_system.all()
            f_datas = []
            for block in blocks:
                f_datas.append(
                    {
                        "block_pk": block.pk,
                        "block_name": block.username,
                    }
                )
            data = {
                "is_block": is_block,
                "f_datas": f_datas,
            }
            return JsonResponse(data)
        return redirect("accounts:detail", user.username)
    return redirect("accounts:login")