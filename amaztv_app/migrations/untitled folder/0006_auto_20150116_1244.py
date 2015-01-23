# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amaztv_app', '0005_auto_20150114_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='description',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
