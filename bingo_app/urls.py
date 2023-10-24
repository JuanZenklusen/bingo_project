from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sorteo/', views.sorteo, name='sorteo'), #para que la gente siga el sorteo
    path('bingo/', views.bingo, name='bingo'), #para sortear
]
