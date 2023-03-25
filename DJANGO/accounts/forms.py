from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from django import forms


class CreateUser(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
        ]
        labels = {
            "username": "아이디",
            "email": "이메일 ",
        }