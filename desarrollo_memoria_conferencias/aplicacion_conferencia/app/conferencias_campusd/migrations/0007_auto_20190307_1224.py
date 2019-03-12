# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('conferencias_campusd', '0006_auto_20190122_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conferencia',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 7, 12, 24, 6, 143187)),
        ),
        migrations.AlterField(
            model_name='intervalo',
            name='id_sinc',
            field=models.OneToOneField(to='conferencias_campusd.Sincronizacion'),
        ),
        migrations.AlterField(
            model_name='sincronizacion',
            name='conferencia',
            field=models.OneToOneField(to='conferencias_campusd.Conferencia'),
        ),
    ]
