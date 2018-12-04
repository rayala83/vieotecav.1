# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('videos_de_conferencias', '0009_auto_20180928_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 3, 9, 49, 33, 853450)),
        ),
    ]
