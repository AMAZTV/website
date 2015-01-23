# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amaztv_app', '0003_auto_20141130_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='thumbnail',
            field=models.CharField(max_length=2000),
            preserve_default=True,
        ),
    ]
