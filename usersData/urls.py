from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from . import views

urlpatterns = [
    path('usuarios', views.get_all_users), #(GET)Necessário para elaboração do ranking
    path('usercards/<str:username>', views.get_user_cards),
    path('usuarios/<str:username>', views.get_user), #(GET)Retornará informações referentes a apenas um usuário (nome,cartas, vitorias, moedas...)
    path('after_battle/<str:username>', views.after_battle), #POST, permite registrar novas informações após uma batalha (se perdeu, venceu, ganhou ou perdeu moedas)
    path('after_pack/<str:username>', views.after_pack),#POST, permite registrar após abertura de um pack, o valor agora de moedas, a nova carta adquirida...
]