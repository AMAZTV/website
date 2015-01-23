# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('category', models.CharField(max_length=30, choices=[(b'Music', b'Music'), (b'Movie', b'Movie'), (b'TV', b'TV'), (b'Fashion', b'Fashion'), (b'LifeStyle', b'LifeStyle')])),
                ('sourceUrl', models.URLField(max_length=500)),
                ('description', models.TextField()),
                ('embed_link', models.TextField(max_length=2000)),
                ('tags', models.CharField(max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
