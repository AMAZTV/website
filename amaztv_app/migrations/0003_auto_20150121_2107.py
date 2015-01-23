# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amaztv_app', '0002_posts_post_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='embed_link',
            field=models.TextField(max_length=2000, blank=True),
            preserve_default=True,
        ),
    ]
