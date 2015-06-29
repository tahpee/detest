# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detest_ui', '0004_nodes_hierarchy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Node_Types',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='nodes_hierarchy',
            name='node_type_id',
            field=models.ForeignKey(to='detest_ui.Node_Types'),
            preserve_default=True,
        ),
    ]
