# Generated by Django 4.2.6 on 2023-10-24 05:16

import bingo_app.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bingo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sorteo',
            name='bolillero',
            field=models.CharField(default=bingo_app.models.default_bolillero, max_length=400, validators=[django.core.validators.RegexValidator('^([1-9][0-9]?|90)(,[1-9][0-9]?|,90)*$', 'Introduzca una lista de números del 1 al 90 separados por comas.')]),
        ),
    ]
