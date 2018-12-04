# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('presentacion_de_conferencias', '0006_auto_20180926_1019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diapositiva',
            name='url_video',
        ),
        migrations.AlterField(
            model_name='diapositiva',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 26, 11, 22, 38, 508104)),
        ),
    ]
