# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('videos_de_conferencias', '0004_auto_20180830_1302'),
    ]

    operations = [
        migrations.DeleteModel(
            name='url_video',
        ),
        migrations.AlterField(
            model_name='video',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 14, 11, 43, 7, 723308)),
        ),
    ]
