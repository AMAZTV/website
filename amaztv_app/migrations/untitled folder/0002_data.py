# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amaztv_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('category', models.CharField(max_length=30, choices=[(b'Music', b'Music'), (b'Movie', b'Movie'), (b'TV', b'TV'), (b'Fashion', b'Fashion'), (b'LifeStyle', b'LifeStyle')])),
                ('up_file', models.FileField(max_length=500, upload_to=b'')),
                ('tags', models.CharField(max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
