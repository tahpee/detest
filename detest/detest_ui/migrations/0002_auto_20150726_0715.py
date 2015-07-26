# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detest_ui', '0001_squashed_0009_auto_20150712_0635'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testsuite_CT',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='node_hierarchy',
            name='node_type_id',
        ),
        migrations.AddField(
            model_name='testcase',
            name='testsuite_id',
            field=models.ForeignKey(default=0, to='detest_ui.Testsuite'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testsuite',
            name='project_id',
            field=models.ForeignKey(default=0, to='detest_ui.Project'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Node_Hierarchy',
        ),
        migrations.DeleteModel(
            name='Node_Type',
        ),
        migrations.AddField(
            model_name='testsuite_ct',
            name='child_id',
            field=models.ForeignKey(related_name='child_testsuite', to='detest_ui.Testsuite'),
        ),
        migrations.AddField(
            model_name='testsuite_ct',
            name='parent_id',
            field=models.ForeignKey(related_name='parent_testsuite', to='detest_ui.Testsuite'),
        ),
    ]
