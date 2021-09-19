from django.db import models

# Create your models here.

class Inventory(models.Model):
    name = models.CharField(max_length=100)
    layout = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    angle = models.CharField(max_length=20)
    switches = models.CharField(max_length=100)
    keycaps = models.CharField(max_length=100)
    plate = models.CharField(max_length=100)
    price = models.CharField(max_length=10)