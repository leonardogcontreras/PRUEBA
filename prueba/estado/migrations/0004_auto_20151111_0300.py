# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estado', '0003_auto_20151110_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estado',
            name='Status',
        ),
        migrations.RemoveField(
            model_name='estado',
            name='recompenza',
        ),
    ]
