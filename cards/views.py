from django.shortcuts import render
from .models import Cards
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from django.http import Http404
from .serializers import CardsSerializer
from requisitions import Request
from .serializers import MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
import random
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def testEndPoint(request):
    if request.method == 'GET':
        data = f"Congratulation {request.user}, your API just responded to GET request"
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = request.POST.get('text')
        data = f'Congratulation your API just responded to POST request with text: {text}'
        return Response({'response': data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token/',
        '/api/register/',
        '/api/token/refresh/'
    ]

@api_view(['GET'])
def get_all_cards(request):
    try:
        cards=Cards.objects.all()
    except:
        raise Http404
    serialized_note= CardsSerializer(cards,many=True)
    return Response(serialized_note.data)

@api_view(['GET'])
def get_comum(request):
    try:
        cards=Cards.objects.filter(rarity="Comum")
        card = random.choice(cards)
    except:
        raise Http404
    serialized_note= CardsSerializer(card)
    return Response(serialized_note.data)

@api_view(['GET'])
def get_especial(request):
    try:
        cards=Cards.objects.filter(rarity="Especial")
        card = random.choice(cards)
    except:
        raise Http404
    serialized_note= CardsSerializer(card)
    return Response(serialized_note.data)

@api_view(['GET'])
def get_random(request):
    try:
        cards=Cards.objects.order_by('?').all()[:3]
    except:
        raise Http404
    serialized_note= CardsSerializer(cards,many=True)
    return Response(serialized_note.data)

@api_view(['GET'])
def get_raro(request):
    try:
        cards=Cards.objects.filter(rarity="Raro")
        card = random.choice(cards)
    except:
        raise Http404
    serialized_note= CardsSerializer(card)
    return Response(serialized_note.data)

@api_view(['GET'])
def get_attack1(request):
    try:
        cards=Cards.objects.filter(attack=1)
        if cards.count()==0:
            requisition = Request().get_attack_1()
            for data in requisition['Battlegrounds']:
                if ('health' in list(data.keys()) and 'img' in list(data.keys())):
                    card=Cards(name=data['name'],image=data["img"],attack=data['attack'],
                    health=data['health'],rarity="Comum")
                    card.save()
            for data in requisition['Core']:
                print(data.keys())
                if ('health' in list(data.keys()) and 'img' in list(data.keys())):
                    card=Cards(name=data['name'],image=data["img"],attack=data['attack'],
                    health=data['health'],rarity="Comum")
                    card.save()
    except:
        raise Http404
    finally:
        cards=Cards.objects.filter(attack=1)

    serialized_note= CardsSerializer(cards,many=True)
    return Response(serialized_note.data)

@api_view(['GET'])
def get_attack2(request):
    try:
        cards=Cards.objects.filter(attack=2)
        if cards.count()==0:
            requisition = Request().get_attack_2()
            for data in requisition['Battlegrounds']:
                if Cards.objects.filter(attack=2).count()<25 and ('health' in list(data.keys()) and 'img' in list(data.keys())):
                    card=Cards(name=data['name'],image=data["img"],attack=data['attack'],
                    health=data['health'],rarity="Comum")
                    card.save()
    except:
        raise Http404
    finally:
        cards=Cards.objects.filter(attack=2)

    serialized_note= CardsSerializer(cards,many=True)
    return Response(serialized_note.data)

@api_view(['GET'])
def get_attack3(request):
    try:
        cards=Cards.objects.filter(attack=3)
        if cards.count()==0:
            requisition = Request().get_attack_3()
            for data in requisition['Battlegrounds']:
                if Cards.objects.filter(attack=3).count()<25 and ('health' in list(data.keys()) and 'img' in list(data.keys())):
                    card=Cards(name=data['name'],image=data["img"],attack=data['attack'],
                    health=data['health'],rarity="Comum")
                    card.save()
    except:
        raise Http404
    finally:
        cards=Cards.objects.filter(attack=3)

    serialized_note= CardsSerializer(cards,many=True)
    return Response(serialized_note.data)

@api_view(['GET'])
def get_attack4(request):
    try:
        cards=Cards.objects.filter(attack=4)
        if cards.count()==0:
            requisition = Request().get_attack_4()
            for data in requisition['Battlegrounds']:
                if Cards.objects.filter(attack=4).count()<20 and ('health' in list(data.keys()) and 'img' in list(data.keys())):
                    card=Cards(name=data['name'],image=data["img"],attack=data['attack'],
                    health=data['health'],rarity="Comum")
                    card.save()
    except:
        raise Http404
    finally:
        cards=Cards.objects.filter(attack=4)

    serialized_note= CardsSerializer(cards,many=True)
    return Response(serialized_note.data)

@api_view(['GET'])
def get_attack5(request):
    try:
        cards=Cards.objects.filter(attack=5)
        if cards.count()==0:
            requisition = Request().get_attack_5()
            for data in requisition['Battlegrounds']:
                if Cards.objects.filter(attack=5).count()<20 and ('health' in list(data.keys()) and 'img' in list(data.keys())):
                    card=Cards(name=data['name'],image=data["img"],attack=data['attack'],
                    health=data['health'],rarity="Especial")
                    card.save()
    except:
        raise Http404
    finally:
        cards=Cards.objects.filter(attack=5)

    serialized_note= CardsSerializer(cards,many=True)
    return Response(serialized_note.data)

@api_view(['GET'])
def get_attack6(request):
    try:
        cards=Cards.objects.filter(attack=6)
        if cards.count()==0:
            requisition = Request().get_attack_6()
            for data in requisition['Battlegrounds']:
                if Cards.objects.filter(attack=6).count()<15 and ('health' in list(data.keys()) and 'img' in list(data.keys())):
                    card=Cards(name=data['name'],image=data["img"],attack=data['attack'],
                    health=data['health'],rarity="Especial")
                    card.save()
    except:
        raise Http404
    finally:
        cards=Cards.objects.filter(attack=6)

    serialized_note= CardsSerializer(cards,many=True)
    return Response(serialized_note.data)

@api_view(['GET'])
def get_attack7(request):
    try:
        cards=Cards.objects.filter(attack=7)
        if cards.count()==0:
            requisition = Request().get_attack_7()
            for data in requisition['Battlegrounds']:
                if ('health' in list(data.keys()) and 'img' in list(data.keys())):
                    card=Cards(name=data['name'],image=data["img"],attack=data['attack'],
                    health=data['health'],rarity="Especial")
                    card.save()
            for data in requisition['Ashes of Outland']:
                if ('health' in list(data.keys()) and 'img' in list(data.keys())):
                    card=Cards(name=data['name'],image=data["img"],attack=data['attack'],
                    health=data['health'],rarity="Especial")
                    card.save()
    except:
        raise Http404
    finally:
        cards=Cards.objects.filter(attack=7)

    serialized_note= CardsSerializer(cards,many=True)
    return Response(serialized_note.data)

@api_view(['GET'])
def get_attack8(request):
    try:
        cards=Cards.objects.filter(attack=8)
        if cards.count()==0:
            requisition = Request().get_attack_8()
            for data in requisition['Battlegrounds']:
                if Cards.objects.filter(attack=8).count()<15 and ('health' in list(data.keys()) and 'img' in list(data.keys())):
                    card=Cards(name=data['name'],image=data["img"],attack=data['attack'],
                    health=data['health'],rarity="Especial")
                    card.save()
    except:
        raise Http404
    finally:
        cards=Cards.objects.filter(attack=8)

    serialized_note= CardsSerializer(cards,many=True)
    return Response(serialized_note.data)

@api_view(['GET'])
def get_attack9(request):
    try:
        cards=Cards.objects.filter(attack=9)
        if cards.count()==0:
            requisition = Request().get_attack_9()
            for data in requisition['Battlegrounds']:
                if ('health' in list(data.keys()) and 'img' in list(data.keys())):
                    card=Cards(name=data['name'],image=data["img"],attack=data['attack'],
                    health=data['health'],rarity="Raro")
                    card.save()
            for data in requisition['Ashes of Outland']:
                if ('health' in list(data.keys()) and 'img' in list(data.keys())):
                    card=Cards(name=data['name'],image=data["img"],attack=data['attack'],
                    health=data['health'],rarity="Raro")
                    card.save()
    except:
        raise Http404
    finally:
        cards=Cards.objects.filter(attack=9)

    serialized_note= CardsSerializer(cards,many=True)
    return Response(serialized_note.data)

@api_view(['GET'])
def get_attack10(request):
    try:
        cards=Cards.objects.filter(attack=10)
        if cards.count()==0:
            requisition = Request().get_attack_10()
            for data in requisition['Battlegrounds']:
                if Cards.objects.filter(attack=10).count()<13 and ('health' in list(data.keys()) and 'img' in list(data.keys())):
                    card=Cards(name=data['name'],image=data["img"],attack=data['attack'],
                    health=data['health'],rarity="Raro")
                    card.save()
    except:
        raise Http404
    finally:
        cards=Cards.objects.filter(attack=10)

    serialized_note= CardsSerializer(cards,many=True)
    return Response(serialized_note.data)

@api_view(['GET'])
def get_attack12(request):
    try:
        cards=Cards.objects.filter(attack=12)
        if cards.count()==0:
            requisition = Request().get_attack_12()
            for data in requisition['Battlegrounds']:
                if Cards.objects.filter(attack=12).count()<5 and ('health' in list(data.keys()) and 'img' in list(data.keys())):
                    card=Cards(name=data['name'],image=data["img"],attack=data['attack'],
                    health=data['health'],rarity="Raro")
                    card.save()
    except:
        raise Http404
    finally:
        cards=Cards.objects.filter(attack=12)

    serialized_note= CardsSerializer(cards,many=True)
    return Response(serialized_note.data)