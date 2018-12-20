# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('presentacion_de_conferencias', '0001_initial'),
        ('videos_de_conferencias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=300)),
                ('jerarquia', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Conferencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(default=datetime.datetime(2018, 12, 6, 9, 50, 46, 349245))),
                ('titulo', models.CharField(max_length=30, null=True)),
                ('autor', models.CharField(max_length=50, null=True)),
                ('descripcion', models.CharField(max_length=500, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('categoria', models.ForeignKey(to='conferencias_campusd.Categoria', null=True)),
                ('ppt', models.ForeignKey(to='presentacion_de_conferencias.Diapositiva')),
            ],
            options={
                'ordering': ['fecha'],
                'verbose_name_plural': 'Conferencias',
            },
        ),
        migrations.CreateModel(
            name='intervalo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('acomulado', models.CharField(max_length=100)),
                ('fin', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['id_slide_ppt'],
                'verbose_name_plural': 'Intervalos',
            },
        ),
        migrations.CreateModel(
            name='Sincronizacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('conferencia', models.ForeignKey(to='conferencias_campusd.Conferencia')),
            ],
            options={
                'ordering': ['conferencia'],
                'verbose_name_plural': 'Sincronizaciones',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.AddField(
            model_name='intervalo',
            name='id_sinc',
            field=models.ForeignKey(to='conferencias_campusd.Sincronizacion'),
        ),
        migrations.AddField(
            model_name='intervalo',
            name='id_slide_ppt',
            field=models.ForeignKey(to='presentacion_de_conferencias.slides_ppt'),
        ),
        migrations.AddField(
            model_name='conferencia',
            name='tags',
            field=models.ManyToManyField(to='conferencias_campusd.Tags'),
        ),
        migrations.AddField(
            model_name='conferencia',
            name='video',
            field=models.ForeignKey(to='videos_de_conferencias.Video'),
        ),
    ]
