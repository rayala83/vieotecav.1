# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('conferencias_campusd', '0004_auto_20190122_0956'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='intervalo',
            options={'verbose_name_plural': 'Intervalos'},
        ),
        migrations.RenameField(
            model_name='intervalo',
            old_name='acomulado',
            new_name='inicio',
        ),
        migrations.RemoveField(
            model_name='conferencia',
            name='ppt',
        ),
        migrations.RemoveField(
            model_name='conferencia',
            name='video',
        ),
        migrations.RemoveField(
            model_name='intervalo',
            name='id_slide_ppt',
        ),
        migrations.AlterField(
            model_name='conferencia',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 22, 13, 3, 7, 140344)),
        ),
    ]
