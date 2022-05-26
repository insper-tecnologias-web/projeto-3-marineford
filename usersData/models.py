from django.db import models

# Create your models here.

class userData(models.Model):
    newUser = models.BooleanField(default=True)
    username = models.CharField(max_length=200)
    cards = models.CharField(max_length=500, default="")
    money = models.IntegerField(default=0)
    win = models.IntegerField(default=0)
    defeat = models.IntegerField(default=0)