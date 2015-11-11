# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0002_auto_20151110_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil_mascota',
            name='nombre',
            field=models.CharField(default=2, max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='perfil_mascota',
            name='color',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='perfil_mascota',
            name='descripcion',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='perfil_mascota',
            name='raza',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='perfil_mascota',
            name='sexo',
            field=models.CharField(max_length=25),
        ),
    ]
