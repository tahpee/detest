# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detest_ui', '0005_testcase_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcase',
            name='preconditions',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='summary',
            field=models.TextField(null=True),
        ),
    ]
