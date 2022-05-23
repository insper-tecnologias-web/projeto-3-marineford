from rest_framework import serializers
from .models import userData


class userDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = userData
        fields = ['id', 'username', 'cards', 'money']