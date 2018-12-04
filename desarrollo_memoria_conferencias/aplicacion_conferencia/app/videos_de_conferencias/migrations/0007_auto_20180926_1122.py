# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('videos_de_conferencias', '0006_auto_20180926_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='url_video',
            field=models.URLField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='video',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 26, 11, 22, 38, 434914)),
        ),
    ]
