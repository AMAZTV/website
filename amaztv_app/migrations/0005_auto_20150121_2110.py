# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amaztv_app', '0004_auto_20150121_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='img_link',
            field=models.ImageField(max_length=1000, upload_to=b'./amaztv_app/static/data/', blank=True),
            preserve_default=True,
        ),
    ]
