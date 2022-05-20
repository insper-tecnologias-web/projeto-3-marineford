from django.shortcuts import render
# Create your views here.
from .models import Cards
from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from django.http import Http404
from .serializers import CardsSerializer
from requisitions import Request


@api_view(['GET'])
def get_all_cards(request):
    try:
        cards=Cards.objects.all()
    except:
        raise Http404
    serialized_note= CardsSerializer(cards,many=True)
    return Response(serialized_note.data)

@api_view(['GET'])
def get_attack1(request):
    try:
        cards=Cards.objects.all()
        print(cards.count())
        if cards.count()==0:
            request=Request().get_attack_1()
            for data in request['Classic']:
                print(data)
                image = Request().remove_bg(data["img"])
                print(image)
                card=Cards(name=data['name'],image=image,attack=data['attack'],
                health=data['health'],rarity="Comum")
                card.save()
            # for data in request['Hall of Fame']:
            #     image = Request().remove_bg(data["img"])
            #     card=Cards(name=data['name'],image=image,attack=data['attack'],
            #     health=data['health'],rarity="Comum")
            #     card.save()
    except:
        raise Http404
    finally:
        cards=Cards.objects.all()

    serialized_note= CardsSerializer(cards,many=True)
    print(serialized_note.data)
    return Response(serialized_note.data)