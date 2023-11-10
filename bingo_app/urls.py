from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sorteo/', views.sorteo, name='sorteo'), #para que la gente siga el sorteo
    path('bingo/', views.bingo, name='bingo'), #para sortear
    path('premios/', views.premios, name='premios'),
    path('alera_bingo/', views.alerta_bingo, name="alerta_bingo"),
    path('alera_linea/', views.alerta_linea, name="alerta_linea"),
]
