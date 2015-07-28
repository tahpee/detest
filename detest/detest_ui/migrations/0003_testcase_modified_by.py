# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('detest_ui', '0002_auto_20150726_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='testcase',
            name='modified_by',
            field=models.ForeignKey(related_name='testcase_modified_by', to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
