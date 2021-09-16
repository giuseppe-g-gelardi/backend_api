from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

