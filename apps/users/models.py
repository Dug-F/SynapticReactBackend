from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.core.models import MyManager

class User(AbstractUser):
    pass

class UserExtension(models.Model):
    objects=MyManager()
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, verbose_name="User")
