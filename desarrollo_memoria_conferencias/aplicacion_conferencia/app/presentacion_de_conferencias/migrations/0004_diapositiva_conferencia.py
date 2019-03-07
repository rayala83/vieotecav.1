# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conferencias_campusd', '0005_auto_20190122_1305'),
        ('presentacion_de_conferencias', '0003_diapositiva_xml'),
    ]

    operations = [
        migrations.AddField(
            model_name='diapositiva',
            name='conferencia',
            field=models.OneToOneField(default=1, to='conferencias_campusd.Conferencia'),
            preserve_default=False,
        ),
    ]
