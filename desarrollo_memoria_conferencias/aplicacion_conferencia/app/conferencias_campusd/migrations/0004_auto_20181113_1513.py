# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('conferencias_campusd', '0003_auto_20181026_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conferencia',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 13, 15, 12, 55, 873906)),
        ),
    ]
