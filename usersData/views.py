from django.shortcuts import render, redirect

from cards.models import Cards
from .models import userData,UsersCards
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .serializers import userDataSerializer,UserCardsSerializer
import http.client
import json


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
        user, created = userData.objects.get_or_create(username=username)
        if created:
            user.username = username
            user.money = 0
            user.win = 0
            user.defeat = 0
            user.save()
    except:
        raise Http404
    finally:    
        user = userData.objects.get(username=username)
        serialized_user= userDataSerializer(user)
        return Response(serialized_user.data)

@api_view(['GET'])
def get_user_cards(request, username):
    try:
        cards = UsersCards.objects.filter(username=username)
        if cards.count()==0:
            for card in Cards.objects.order_by('?').filter(rarity="Comum")[:5]:
                new_card = UsersCards(username=username,name=card.name,image=card.image,
                attack=card.attack,health=card.health,rarity=card.rarity)
                new_card.save()
    except:
        raise Http404
    finally:    
        cards = UsersCards.objects.filter(username=username)
        serialized_user= UserCardsSerializer(cards,many=True)
        return Response(serialized_user.data)

@api_view(['POST'])
def after_battle(request, username):
    try:
        user = userData.objects.get(username=username)
        new_user_data = request.data
        user.money = new_user_data['money'] + user.money
        user.win = new_user_data['win'] + user.win
        user.defeat = new_user_data['defeat'] + user.defeat
        user.save()
        user = userData.objects.get(username=username)
        if user.money<0:
            user.money = 0
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
        user.money = user.money + new_user_data['money']
        id = new_user_data['id']
        card = Cards.objects.get(id=id)
        new_card = UsersCards(username=username,name=card.name,image=card.image,
        attack=card.attack,health=card.health,rarity=card.rarity)
        new_card.save()
        user.save()
        if user.money<0:
            user.money = 0
            user.save()
    except:
        raise Http404
    serialized_user = userDataSerializer(user)
    return Response(serialized_user.data)

