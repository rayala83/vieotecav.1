# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('presentacion_de_conferencias', '0004_auto_20180830_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='diapositiva',
            name='url_video',
            field=models.URLField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='diapositiva',
            name='diapo',
            field=models.FileField(upload_to=b'media'),
        ),
        migrations.AlterField(
            model_name='diapositiva',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 14, 11, 43, 7, 798981)),
        ),
    ]
