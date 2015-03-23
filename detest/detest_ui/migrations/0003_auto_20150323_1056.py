# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detest_ui', '0002_projects_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
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
        migrations.DeleteModel(
            name='Projects',
        ),
    ]
