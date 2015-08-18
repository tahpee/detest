# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detest_ui', '0008_auto_20150803_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='notes',
            field=models.TextField(default=b'', null=True),
        ),
    ]
