# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('conferencias_campusd', '0004_auto_20181113_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conferencia',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 22, 11, 50, 16, 452478)),
        ),
    ]
