# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0004_remove_perfil_mascota_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil_mascota',
            name='foto',
            field=models.ImageField(default=1, upload_to=b''),
            preserve_default=False,
        ),
    ]
