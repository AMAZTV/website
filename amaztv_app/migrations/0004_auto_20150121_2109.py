# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amaztv_app', '0003_auto_20150121_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='img_link',
            field=models.ImageField(default=str, max_length=1000, upload_to=b'./amaztv_app/static/data/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='posts',
            name='thumbnail',
            field=models.FileField(max_length=1000, upload_to=b'./amaztv_app/static/data/'),
            preserve_default=True,
        ),
    ]
