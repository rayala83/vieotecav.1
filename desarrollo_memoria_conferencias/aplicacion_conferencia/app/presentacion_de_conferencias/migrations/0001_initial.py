# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diapositiva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(default=datetime.datetime(2018, 8, 13, 12, 9, 28, 299928))),
                ('titulo', models.CharField(max_length=30)),
                ('diapo', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['fecha'],
                'verbose_name_plural': 'Diapositivas',
            },
        ),
    ]
