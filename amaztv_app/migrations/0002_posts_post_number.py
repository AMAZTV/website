# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amaztv_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='post_number',
            field=models.IntegerField(default=int),
            preserve_default=False,
        ),
    ]
