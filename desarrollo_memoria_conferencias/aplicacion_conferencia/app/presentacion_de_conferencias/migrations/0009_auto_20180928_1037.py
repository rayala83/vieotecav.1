# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('videos_de_conferencias', '0009_auto_20180928_1037'),
        ('presentacion_de_conferencias', '0008_auto_20180927_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='diapositiva',
            name='url',
            field=models.ForeignKey(default=1, to='videos_de_conferencias.Video'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='diapositiva',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 28, 10, 37, 18, 744779)),
        ),
    ]
