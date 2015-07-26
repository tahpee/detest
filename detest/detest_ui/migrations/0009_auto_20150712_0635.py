# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detest_ui', '0008_auto_20150712_0634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
