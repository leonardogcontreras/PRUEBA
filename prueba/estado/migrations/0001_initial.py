# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0004_remove_perfil_mascota_foto'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('status', '0002_remove_status_recompensa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('recompenza', models.IntegerField()),
                ('Mascota', models.ForeignKey(to='mascota.Perfil_Mascota', null=True)),
                ('Status', models.ForeignKey(to='status.Status', null=True)),
                ('Usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
