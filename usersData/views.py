from curses.ascii import HT
from django.shortcuts import render, redirect
from .models import userData
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .serializers import userDataSerializer
import json

# Create your views here.

#abertura de peck de carta
# win & defeat

# O resto do código continua aqui pra cima

@api_view(['GET'])
def get_all_users(request):
    try:
        users=userData.objects.all()
    except:
        raise Http404
    serialized_users= userDataSerializer(users,many=True)
    return Response(serialized_users.data)

@api_view(['GET'])
def get_user(request, username):
    try:
        user, created = userData.objects.get_or_create(username)
        if created:
            user.username = username
            user.cards = initial_cards()
            user.coins = 0
            user.win = 0
            user.defeat = 0
    except:
        raise Http404
    serialized_user= userDataSerializer(user)
    return Response(serialized_user.data)

@api_view(['POST'])
def after_battle(request, username):
    try:
        user = userData.objects.get(username=username)
        new_user_data = request.data
        user.money = new_user_data['money']
        user.win = new_user_data['win']
        user.defeat = new_user_data['defeat']
        user.save()
    except:
        raise Http404
    serialized_user = userDataSerializer(user)
    return Response(serialized_user.data)

@api_view(['POST'])
def after_pack(request, username):
    try:
        user = userData.objects.get(username=username)
        new_user_data = request.data
        user.money = new_user_data['money']
        cards = json.loads(user.cards)
        if new_user_data['cards'] not in cards:
            cards.append(new_user_data['cards'])
        user.cards = json.dumps(cards)
        user.save()
    except:
        raise Http404
    serialized_user = userDataSerializer(user)
    return Response(serialized_user.data)

