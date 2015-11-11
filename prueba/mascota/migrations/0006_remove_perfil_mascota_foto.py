# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0005_perfil_mascota_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil_mascota',
            name='foto',
        ),
    ]
