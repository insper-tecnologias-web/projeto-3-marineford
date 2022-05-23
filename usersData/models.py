from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=200)
    cards = models.CharField(max_length=500)
    money = models.IntegerField()