from django.db import models

# Create your models here.

class userData(models.Model):
    username = models.CharField(max_length=200)
    cards = models.CharField(max_length=500, default="")
    money = models.IntegerField(default=0)