from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    picture = models.ImageField(default='perfil.jpg',upload_to='users/')
    model = models.BooleanField(default=False)