# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('conferencias_campusd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conferencia',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 26, 11, 5, 56, 24494)),
        ),
    ]
