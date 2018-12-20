# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url_video', models.URLField(max_length=150)),
                ('duracion', models.CharField(max_length=100)),
                ('imagen', models.ImageField(upload_to=b'img_youtube')),
            ],
            options={
                'ordering': ['url_video'],
                'verbose_name_plural': 'Videos',
            },
        ),
    ]
