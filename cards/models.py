from django.db import models

# Create your models here.
class Cards(models.Model):
    name = models.TextField(default=" ",null=True)
    image = models.BinaryField()
    attack = models.IntegerField(default=0,null=True)
    health = models.IntegerField(default=0,null=True)
    rarity = models.CharField(max_length=200)
    def __str__(self):
        return (self.name)