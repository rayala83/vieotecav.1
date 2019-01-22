# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('conferencias_campusd', '0002_auto_20181210_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conferencia',
            name='autor',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='conferencia',
            name='categoria',
            field=models.ForeignKey(default=1, to='conferencias_campusd.Categoria'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='conferencia',
            name='descripcion',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='conferencia',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 9, 48, 56, 511965)),
        ),
        migrations.AlterField(
            model_name='conferencia',
            name='titulo',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
