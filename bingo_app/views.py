from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from .models import Sorteo, Sorteo_Numeros
import random
from django.core.exceptions import ObjectDoesNotExist

def es_superusuario(user):
    return user.is_superuser


def index(request):
    return render(request, 'partials/index_content.html', {})

def sorteo(request):
    sorteo_obj = Sorteo.objects.last()  # Obtén el ultimo objeto Sorteo
    bol = sorteo_obj.bolillero
    nro = sorteo_obj.numero_sorteado
    numeros_sorteados = sorteo_obj.numeros_sorteados

    if nro is not None:
        int_nro = int(nro)
    else:
        int_nro = ""

    if numeros_sorteados is "":
        nro_sort = ""
        ult5 = ""
    else:
        lista_ultimos_sorteados = numeros_sorteados.split(",")
        nro_sort = [int(numero) for numero in lista_ultimos_sorteados]
        ult5 = nro_sort[-10:]
    return render(request, 'partials/sorteo.html', {'bol': bol, 'int_nro': int_nro, 'ult5': ult5, 'nro_sort': nro_sort})



@user_passes_test(es_superusuario, login_url='/sorteo')
def bingo(request):
    sorteo_obj = Sorteo.objects.last()  # Obtén el ultimo objeto Sorteo
    bol_a = sorteo_obj.bolillero
    bol = bol_a.split(",")

    nro = sorteo_obj.numero_sorteado
    numeros_sorteados = sorteo_obj.numeros_sorteados

    if nro is not None:
        int_nro = int(nro)
    else:
        int_nro = ""

    if numeros_sorteados is "":
        nro_sort = ""
        ult5 = ""
    else:
        lista_ultimos_sorteados = numeros_sorteados.split(",")
        nro_sort = [int(numero) for numero in lista_ultimos_sorteados]
        ult5 = nro_sort[-6:-1]
        

    if request.method == 'POST':
        if 'siguiente' in request.POST:
            numero_siguiente = sorteo_obj.siguiente_numero()
            return redirect('bingo')

    return render(request, 'partials/bingo.html', {'bol': bol, 'int_nro': int_nro, 'ult5': ult5, 'nro_sort': nro_sort})


@user_passes_test(es_superusuario, login_url='/sorteo')
def premios(request):
    sorteo_obj = Sorteo_Numeros.objects.last()  # Obtén el ultimo objeto Sorteo
    bol_a = sorteo_obj.bolillero
    bol = bol_a.split(",")

    nro = sorteo_obj.numero_sorteado
    numeros_sorteados = sorteo_obj.numeros_sorteados

    if nro is not None:
        int_nro = int(nro)
    else:
        int_nro = ""

    if numeros_sorteados is "":
        nro_sort = ""
        ult5 = ""
    else:
        lista_ultimos_sorteados = numeros_sorteados.split(",")
        nro_sort = [int(numero) for numero in lista_ultimos_sorteados]
        ult5 = nro_sort[-6:-1]

    if request.method == 'POST':
        if 'siguientee' in request.POST:
            numero_siguiente = sorteo_obj.siguiente_numero()
            return redirect('premios')

    return render(request, 'partials/premios.html', {'bol': bol, 'int_nro': int_nro, 'ult5': ult5, 'nro_sort': nro_sort})


@user_passes_test(es_superusuario, login_url='/sorteo')
def alerta_bingo(request):
    return render(request, 'partials/alerta_bingo.html', {})


@user_passes_test(es_superusuario, login_url='/sorteo')
def alerta_linea(request):
    return render(request, 'partials/alerta_linea.html', {})