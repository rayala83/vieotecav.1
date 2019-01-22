# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('conferencias_campusd', '0003_auto_20190121_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conferencia',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 22, 9, 55, 59, 77239)),
        ),
        migrations.AlterField(
            model_name='conferencia',
            name='ppt',
            field=models.OneToOneField(to='presentacion_de_conferencias.Diapositiva'),
        ),
        migrations.AlterField(
            model_name='conferencia',
            name='video',
            field=models.OneToOneField(to='videos_de_conferencias.Video'),
        ),
    ]
