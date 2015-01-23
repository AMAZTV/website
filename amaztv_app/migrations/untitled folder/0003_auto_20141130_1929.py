# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amaztv_app', '0002_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='thumbnail',
            field=models.URLField(default='None', max_length=2000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='data',
            name='up_file',
            field=models.FileField(max_length=500, upload_to=b'./amaztv_app/static/data/'),
            preserve_default=True,
        ),
    ]
