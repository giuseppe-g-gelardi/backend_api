from django.db import models
from django.contrib.auth.models import User

class Keyboards(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default =None)
    layout = models.CharField(max_length=50, default=None)
    color = models.CharField(max_length=50, default=None)
    keycap_color = models.CharField(max_length=50, default=None)

    
