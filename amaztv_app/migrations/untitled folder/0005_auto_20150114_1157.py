# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amaztv_app', '0004_auto_20141201_2125'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Data',
        ),
        migrations.AlterField(
            model_name='posts',
            name='category',
            field=models.CharField(max_length=30, choices=[(b'Music', b'Music'), (b'Movie', b'Movie'), (b'TV', b'TV'), (b'LifeStyle', b'LifeStyle')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='posts',
            name='thumbnail',
            field=models.FileField(max_length=500, upload_to=b'./amaztv_app/static/data/'),
            preserve_default=True,
        ),
    ]
