# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('estado', '0002_auto_20151110_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estado',
            name='Mascota',
            field=models.ForeignKey(default=1, to='mascota.Perfil_Mascota'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='estado',
            name='Usuario',
            field=models.ForeignKey(default=2, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
