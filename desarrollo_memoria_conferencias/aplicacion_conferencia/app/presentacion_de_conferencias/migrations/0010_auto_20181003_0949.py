# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('presentacion_de_conferencias', '0009_auto_20180928_1037'),
    ]

    operations = [
        migrations.CreateModel(
            name='imagen_ppt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', models.ImageField(upload_to=b'media')),
            ],
        ),
        migrations.AlterField(
            model_name='diapositiva',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 3, 9, 49, 33, 976940)),
        ),
        migrations.AddField(
            model_name='imagen_ppt',
            name='ppt',
            field=models.ForeignKey(to='presentacion_de_conferencias.Diapositiva'),
        ),
    ]
