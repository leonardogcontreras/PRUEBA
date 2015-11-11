# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0003_auto_20151110_1835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil_mascota',
            name='foto',
        ),
    ]
