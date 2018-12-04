# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('presentacion_de_conferencias', '0013_auto_20181026_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diapositiva',
            name='diapo',
            field=models.FileField(upload_to=b'media/ppt'),
        ),
        migrations.AlterField(
            model_name='diapositiva',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 13, 15, 12, 56, 116143)),
        ),
        migrations.AlterField(
            model_name='imagen_ppt',
            name='imagen',
            field=models.ImageField(upload_to=b'media/fotos'),
        ),
    ]
