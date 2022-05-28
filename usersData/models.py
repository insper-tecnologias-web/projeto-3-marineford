from django.db import models

# Create your models here.

class userData(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=200,null=True)
    cards = models.IntegerField(default=0,null=True)
    money = models.IntegerField(default=0,null=True)
    win = models.IntegerField(default=0,null=True)
    defeat = models.IntegerField(default=0,null=True)

    def __str__(self):
        return (self.username)

class UsersCards(models.Model):
    card_id = models.IntegerField(default=0,null=True)
    username = models.CharField(max_length=200,null=True)
    name = models.TextField(default=" ",null=True)
    image = models.TextField(default=" ",null=True)
    attack = models.IntegerField(default=0,null=True)
    health = models.IntegerField(default=0,null=True)
    rarity = models.CharField(max_length=200)
    def __str__(self):
        return (self.name)