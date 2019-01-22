# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presentacion_de_conferencias', '0002_auto_20181210_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='diapositiva',
            name='xml',
            field=models.FileField(default=1, upload_to=b'xml'),
            preserve_default=False,
        ),
    ]
