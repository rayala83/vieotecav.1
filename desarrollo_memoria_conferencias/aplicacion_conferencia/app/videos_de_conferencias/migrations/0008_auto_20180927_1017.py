# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('videos_de_conferencias', '0007_auto_20180926_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 27, 10, 17, 45, 751881)),
        ),
    ]
