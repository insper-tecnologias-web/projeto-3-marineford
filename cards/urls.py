from django.urls import path

from . import views

urlpatterns = [
    path('attack1', views.get_attack1, name='attack1'),
]