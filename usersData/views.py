from django.shortcuts import render, redirect
from .models import userData
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .serializers import userDataSerializer

# Create your views here.

#abertura de peck de carta
# win & defeat

# O resto do código continua aqui pra cima

@api_view(['POST'])
def user_win(request, username, money):
    try:
        user = userData.objects.get(username=username)
        user.money = money
        user.save()
    except userData.DoesNotExist:
        raise Http404()

@api_view(['POST'])
def user_defeat(request, username, money):
    try:
        user = userData.objects.get(username=username)
        user.money = money
        user.save()
    except userData.DoesNotExist:
        raise Http404()


