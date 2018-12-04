# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conferencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(default=datetime.datetime(2018, 10, 12, 10, 51, 17, 998471))),
                ('video', models.CharField(max_length=300)),
                ('ppt', models.CharField(max_length=300)),
                ('titulo', models.CharField(max_length=300)),
                ('inicio', models.CharField(max_length=100)),
                ('fin', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['fecha'],
            },
        ),
    ]
