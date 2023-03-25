from django.db import models
from django.contrib.auth.models import AbstractUser
from Gotalk.settings import AUTH_USER_MODEL

# Create your models here.

class User(AbstractUser):
    pass