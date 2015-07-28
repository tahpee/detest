# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detest_ui', '0006_auto_20150728_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcase',
            name='estimate',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='modified',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='previous_version',
            field=models.ForeignKey(to='detest_ui.Testcase', null=True),
        ),
    ]
