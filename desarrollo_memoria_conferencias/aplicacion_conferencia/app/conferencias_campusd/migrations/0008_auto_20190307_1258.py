# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('conferencias_campusd', '0007_auto_20190307_1224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sincronizacion',
            name='conferencia',
        ),
        migrations.RemoveField(
            model_name='intervalo',
            name='id_sinc',
        ),
        migrations.AddField(
            model_name='intervalo',
            name='conferencia',
            field=models.OneToOneField(default=1, to='conferencias_campusd.Conferencia'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='conferencia',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 7, 12, 57, 37, 895540)),
        ),
        migrations.DeleteModel(
            name='Sincronizacion',
        ),
    ]
