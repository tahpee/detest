# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('notes', models.TextField(null=True)),
                ('color', models.CharField(max_length=12)),
                ('active', models.IntegerField(default=1)),
                ('prefix', models.CharField(max_length=16)),
                ('tc_counter', models.IntegerField(default=0)),
                ('is_public', models.IntegerField(default=1)),
                ('options', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
