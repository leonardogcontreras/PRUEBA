# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estado', '0004_auto_20151111_0300'),
        ('status', '0002_remove_status_recompensa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mascotas_Perdidas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('recompenza', models.IntegerField()),
                ('estado', models.ForeignKey(to='estado.Estado')),
                ('status', models.ForeignKey(to='status.Status')),
            ],
        ),
    ]
