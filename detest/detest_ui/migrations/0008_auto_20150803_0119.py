# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detest_ui', '0007_auto_20150728_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testsuite',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
