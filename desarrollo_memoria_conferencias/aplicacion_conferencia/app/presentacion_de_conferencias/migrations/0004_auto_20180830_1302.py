# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('presentacion_de_conferencias', '0003_auto_20180829_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diapositiva',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 30, 13, 0, 57, 592140)),
        ),
    ]
