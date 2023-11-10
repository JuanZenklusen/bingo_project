from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models

comma_separated_validator = RegexValidator(
    r'^([1-9][0-9]?|90)(,[1-9][0-9]?|,90)*$', 
    'Introduzca una lista de números del 1 al 90 separados por comas.'
)

def default_bolillero():
    return ','.join(map(str, range(1, 91)))



class Sorteo(models.Model):
    bolillero = models.CharField(max_length=400, default=default_bolillero, validators=[comma_separated_validator])
    numero_sorteado = models.IntegerField(blank=True, null=True)
    numeros_sorteados = models.CharField(max_length=1000, blank=True, validators=[comma_separated_validator])

    def __str__(self):
        return f'{self.id}'

    def siguiente_numero(self):
        import random
        if not self.bolillero:
            return None

        bolillero_lista = list(map(int, self.bolillero.split(',')))
        numero_extraido = random.choice(bolillero_lista)
        bolillero_lista.remove(numero_extraido)
        self.bolillero = ','.join(map(str, bolillero_lista))
        self.numero_sorteado = numero_extraido

        if self.numeros_sorteados:
            self.numeros_sorteados += f',{numero_extraido}'
        else:
            self.numeros_sorteados = f'{numero_extraido}'

        self.save()
        return numero_extraido


'''class NumeroSorteado(models.Model):
    numero = models.IntegerField()
    fecha_sorteo = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.numero)'''
    


class Sorteo_Numeros(models.Model):
    numero_maximo = models.IntegerField(blank=False, null=False)
    bolillero = models.CharField(max_length=400, default=None, blank=True, null=True, validators=[comma_separated_validator])
    numero_sorteado = models.IntegerField(blank=True, null=True)
    numeros_sorteados = models.CharField(max_length=1000, blank=True, validators=[comma_separated_validator])

    def save(self, *args, **kwargs):
        if not self.bolillero:
            self.bolillero = self.default_bolillero_2()
        super(Sorteo_Numeros, self).save(*args, **kwargs)

    def default_bolillero_2(self):
        return ','.join(map(str, range(1, self.numero_maximo+1)))

    def __str__(self):
        return f'{self.id}'

    def siguiente_numero(self):
        import random
        if not self.bolillero:
            return None

        bolillero_lista = list(map(int, self.bolillero.split(',')))
        numero_extraido = random.choice(bolillero_lista)
        bolillero_lista.remove(numero_extraido)
        self.bolillero = ','.join(map(str, bolillero_lista))
        self.numero_sorteado = numero_extraido

        if self.numeros_sorteados:
            self.numeros_sorteados += f',{numero_extraido}'
        else:
            self.numeros_sorteados = f'{numero_extraido}'

        self.save()
        return numero_extraido