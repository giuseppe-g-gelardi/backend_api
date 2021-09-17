from django.contrib.auth.models import User
from django.db import models
 
class Keyboards(models.Model):
    layout = models.CharField(max_length=50),
    color = models.CharField(max_length=50),
    keycap_color = models.CharField(max_length=50),
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
