from django.db import models
from keyboards.models import Keyboards


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    keyboard = models.ForeignKey(Keyboards, on_delete=models.CASCADE)