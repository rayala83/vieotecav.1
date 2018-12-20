# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diapositiva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('diapo', models.FileField(upload_to=b'ppt')),
            ],
            options={
                'ordering': ['diapo'],
                'verbose_name_plural': 'Diapositivas',
            },
        ),
        migrations.CreateModel(
            name='slides_ppt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slide', models.ImageField(upload_to=b'slides')),
                ('duracion', models.CharField(max_length=100)),
                ('id_diapo', models.ForeignKey(to='presentacion_de_conferencias.Diapositiva')),
            ],
        ),
    ]
