from django.urls import path

from . import views

urlpatterns = [
    path('all', views.get_all_cards, name='all'),
    path('comum', views.get_comum),
    path('especial', views.get_especial),
    path('raro', views.get_raro),
    path('attack1', views.get_attack1, name='attack1'),
    path('attack2', views.get_attack2, name='attack2'),
    path('attack3', views.get_attack3, name='attack3'),
    path('attack4', views.get_attack4, name='attack4'),
    path('attack5', views.get_attack5, name='attack5'),
    path('attack6', views.get_attack6, name='attack6'),
    path('attack7', views.get_attack7, name='attack7'),
    path('attack8', views.get_attack8, name='attack8'),
    path('attack9', views.get_attack9, name='attack9'),
    path('attack10', views.get_attack10, name='attack10'),
    # path('attack11', views.get_attack11, name='attack11'),
    path('attack12', views.get_attack12, name='attack12'),
]