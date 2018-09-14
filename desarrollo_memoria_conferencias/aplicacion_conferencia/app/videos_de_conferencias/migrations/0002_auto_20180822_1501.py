# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('videos_de_conferencias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 22, 15, 1, 42, 380310)),
        ),
        migrations.AlterField(
            model_name='video',
            name='titulo',
            field=models.CharField(max_length=300),
        ),
    ]
