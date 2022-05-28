from rest_framework import serializers
from .models import userData,UsersCards


class userDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = userData
        fields = ['id', 'username', 'cards', 'money', 'win', 'defeat']

class UserCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model=UsersCards
        fields=['id','card_id','username','name','attack','health','image','rarity']

