# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('detest_ui', '0007_project_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Build',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45)),
                ('notes', models.CharField(max_length=45)),
                ('active', models.SmallIntegerField()),
                ('created', models.DateTimeField()),
                ('released', models.DateTimeField()),
                ('closed', models.DateTimeField()),
                ('author_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Execution_Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Node_Hierarchy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('parent_id', models.IntegerField()),
                ('child_id', models.IntegerField()),
                ('node_order', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project_Platform',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('platform_id', models.ForeignKey(to='detest_ui.Platform')),
            ],
        ),
        migrations.CreateModel(
            name='TCAttachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('filename', models.CharField(max_length=250)),
                ('filepath', models.CharField(max_length=250)),
                ('filesize', models.IntegerField()),
                ('date_added', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TCExecution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('executed', models.DateTimeField()),
                ('duration', models.CharField(max_length=45)),
                ('notes', models.TextField()),
                ('build_id', models.ForeignKey(to='detest_ui.Build')),
                ('platform_id', models.ForeignKey(to='detest_ui.Platform')),
                ('status_id', models.ForeignKey(to='detest_ui.Execution_Status')),
            ],
        ),
        migrations.CreateModel(
            name='TCExecution_Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('execution_type', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='TCPriority',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('priority', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='TCStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Testcase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('external_id', models.IntegerField()),
                ('version', models.IntegerField()),
                ('summary', models.TextField()),
                ('preconditions', models.TextField()),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField()),
                ('requirement', models.CharField(max_length=100)),
                ('author_id', models.ForeignKey(related_name='testcase_authored_by', to=settings.AUTH_USER_MODEL)),
                ('modified_id', models.ForeignKey(related_name='testcase_modified_by', to=settings.AUTH_USER_MODEL)),
                ('previous_version_id', models.ForeignKey(to='detest_ui.Testcase')),
                ('tcexecution_type_id', models.ForeignKey(to='detest_ui.TCExecution_Type')),
                ('tcpriority_id', models.ForeignKey(to='detest_ui.TCPriority')),
                ('tcstatus_id', models.ForeignKey(to='detest_ui.TCStatus')),
            ],
        ),
        migrations.CreateModel(
            name='Testplan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('active', models.SmallIntegerField()),
                ('notes', models.TextField()),
                ('created', models.DateTimeField()),
                ('author_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Testplan_Platforms',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('platform_id', models.ForeignKey(to='detest_ui.Platform')),
                ('testplan_id', models.ForeignKey(to='detest_ui.Testplan')),
            ],
        ),
        migrations.CreateModel(
            name='Testplan_Testcases',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField()),
                ('assigned_id', models.ForeignKey(related_name='testplan_testcases_assigned_to', to=settings.AUTH_USER_MODEL)),
                ('author_id', models.ForeignKey(related_name='testplan_testcases_added_by', to=settings.AUTH_USER_MODEL)),
                ('platform_id', models.ForeignKey(to='detest_ui.Platform')),
                ('testcase_id', models.ForeignKey(to='detest_ui.Testcase')),
                ('testplan_id', models.ForeignKey(to='detest_ui.Testplan')),
            ],
        ),
        migrations.CreateModel(
            name='Teststep',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('step_number', models.IntegerField()),
                ('actions', models.TextField()),
                ('expected_results', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Testsuite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45)),
                ('details', models.TextField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Node_Types',
            new_name='Node_Type',
        ),
        migrations.RemoveField(
            model_name='nodes_hierarchy',
            name='node_type_id',
        ),
        migrations.RemoveField(
            model_name='project',
            name='color',
        ),
        migrations.RemoveField(
            model_name='project',
            name='is_public',
        ),
        migrations.RemoveField(
            model_name='project',
            name='options',
        ),
        migrations.RemoveField(
            model_name='project',
            name='tc_counter',
        ),
        migrations.AddField(
            model_name='project',
            name='public',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='project',
            name='notes',
            field=models.TextField(default=b''),
        ),
        migrations.AlterField(
            model_name='project',
            name='prefix',
            field=models.CharField(max_length=45),
        ),
        migrations.DeleteModel(
            name='Nodes_Hierarchy',
        ),
        migrations.AddField(
            model_name='testplan',
            name='project_id',
            field=models.ForeignKey(to='detest_ui.Project'),
        ),
        migrations.AddField(
            model_name='tcexecution',
            name='testcase_id',
            field=models.ForeignKey(to='detest_ui.Testcase'),
        ),
        migrations.AddField(
            model_name='tcexecution',
            name='tester_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tcexecution',
            name='testplan_id',
            field=models.ForeignKey(to='detest_ui.Testplan'),
        ),
        migrations.AddField(
            model_name='tcattachment',
            name='testcase_id',
            field=models.ForeignKey(to='detest_ui.Testcase'),
        ),
        migrations.AddField(
            model_name='tcattachment',
            name='user_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project_platform',
            name='project_id',
            field=models.ForeignKey(to='detest_ui.Project'),
        ),
        migrations.AddField(
            model_name='node_hierarchy',
            name='node_type_id',
            field=models.ForeignKey(to='detest_ui.Node_Type'),
        ),
        migrations.AddField(
            model_name='build',
            name='testplan_id',
            field=models.ForeignKey(to='detest_ui.Testplan'),
        ),
    ]
