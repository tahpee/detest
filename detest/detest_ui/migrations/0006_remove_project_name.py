# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detest_ui', '0005_auto_20150324_1100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='name',
        ),
    ]
