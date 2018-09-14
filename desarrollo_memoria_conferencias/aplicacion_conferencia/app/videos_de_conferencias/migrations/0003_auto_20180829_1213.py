# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('videos_de_conferencias', '0002_auto_20180822_1501'),
    ]

    operations = [
        migrations.CreateModel(
            name='url_video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url_video', models.URLField(max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Urls',
            },
        ),
        migrations.AlterField(
            model_name='video',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 29, 12, 13, 3, 450601)),
        ),
    ]
