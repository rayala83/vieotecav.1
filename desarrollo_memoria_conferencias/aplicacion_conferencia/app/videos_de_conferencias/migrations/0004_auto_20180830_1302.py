# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('videos_de_conferencias', '0003_auto_20180829_1213'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='video',
            new_name='duracion',
        ),
        migrations.AddField(
            model_name='video',
            name='autor',
            field=models.CharField(default=10, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='imagen',
            field=models.ImageField(default=2, upload_to=b'media'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='video',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 30, 13, 0, 57, 533537)),
        ),
    ]
