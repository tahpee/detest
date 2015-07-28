# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detest_ui', '0003_testcase_modified_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='testcase',
            name='estimate',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
