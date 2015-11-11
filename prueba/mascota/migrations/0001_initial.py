# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil_Mascota',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('foto', models.ImageField(max_length=25, upload_to=b'', blank=True)),
                ('raza', models.CharField(max_length=25, blank=True)),
                ('color', models.CharField(max_length=25, blank=True)),
                ('sexo', models.CharField(max_length=25, blank=True)),
                ('descripcion', models.TextField(max_length=255, blank=True)),
            ],
        ),
    ]
