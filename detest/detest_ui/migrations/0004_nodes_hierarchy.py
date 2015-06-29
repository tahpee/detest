# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detest_ui', '0003_auto_20150323_1056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nodes_Hierarchy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('parent_id', models.IntegerField()),
                ('node_type_id', models.IntegerField()),
                ('node_order', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
