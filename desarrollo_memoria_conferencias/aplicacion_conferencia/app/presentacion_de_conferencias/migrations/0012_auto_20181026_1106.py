# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('presentacion_de_conferencias', '0011_auto_20181012_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagen_ppt',
            name='fin',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='imagen_ppt',
            name='inicio',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='diapositiva',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 26, 11, 5, 56, 331066)),
        ),
    ]
