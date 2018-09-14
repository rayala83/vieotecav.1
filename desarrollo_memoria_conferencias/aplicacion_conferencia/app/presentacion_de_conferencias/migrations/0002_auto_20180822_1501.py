# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('presentacion_de_conferencias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diapositiva',
            name='diapo',
            field=models.FileField(upload_to=b'media/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='diapositiva',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 22, 15, 1, 42, 456528)),
        ),
    ]
