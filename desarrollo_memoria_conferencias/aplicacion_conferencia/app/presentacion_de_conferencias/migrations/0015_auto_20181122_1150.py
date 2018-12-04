# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('presentacion_de_conferencias', '0014_auto_20181113_1513'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diapositiva',
            old_name='url',
            new_name='id_video',
        ),
        migrations.RenameField(
            model_name='imagen_ppt',
            old_name='fin',
            new_name='duracion',
        ),
        migrations.RenameField(
            model_name='imagen_ppt',
            old_name='ppt',
            new_name='id_diapo',
        ),
        migrations.RemoveField(
            model_name='imagen_ppt',
            name='inicio',
        ),
        migrations.AlterField(
            model_name='diapositiva',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 22, 11, 50, 16, 639718)),
        ),
    ]
