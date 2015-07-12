from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=45)
    notes = models.TextField(default="")
    prefix = models.CharField(max_length=45)
    active = models.BooleanField(default=True)
    public = models.BooleanField(default=False)


class Testsuite(models.Model):
    name = models.CharField(max_length=45)
    details = models.TextField()


class TCPriority(models.Model):
    priority = models.CharField(max_length=45)


class TCStatus(models.Model):
    status = models.CharField(max_length=45)


class TCExecution_Type(models.Model):
    execution_type = models.CharField(max_length=45)


# class user(models.Model):
#   id = models.IntegerField()
#   password = models.CharField(max_length=128)
#   last_login = models.DateTimeField()
#   is_superuser = models.SmallIntegerField()
#   username = models.CharField(max_length=30)
#   first_name = models.CharField(max_length=30)
#   last_name = models.CharField(max_length=30)
#   email = models.CharField(max_length=75)
#   is_staff = models.SmallIntegerField()
#   is_active = models.SmallIntegerField()
#   date_joined = models.DateTimeField()


class Testcase(models.Model):
    external_id = models.IntegerField()
    version = models.IntegerField()
    summary = models.TextField()
    preconditions = models.TextField()
    tcpriority_id = models.ForeignKey(TCPriority)
    tcstatus_id = models.ForeignKey(TCStatus)
    tcexecution_type_id = models.ForeignKey(TCExecution_Type)
    author_id = models.ForeignKey(User, related_name="testcase_authored_by")
    modified_id = models.ForeignKey(User, related_name="testcase_modified_by")
    created = models.DateTimeField()
    modified = models.DateTimeField()
    previous_version_id = models.ForeignKey('self')
    requirement = models.CharField(max_length=100)


class Node_Type(models.Model):
    description = models.CharField(max_length=100)


class Node_Hierarchy(models.Model):
    node_type_id = models.ForeignKey(Node_Type)
    parent_id = models.IntegerField()
    child_id = models.IntegerField()
    node_order = models.IntegerField()


class Teststep(models.Model):
    step_number = models.IntegerField()
    actions = models.TextField()
    expected_results = models.TextField()


class TCAttachment(models.Model):
    testcase_id = models.ForeignKey(Testcase)
    title = models.CharField(max_length=250)
    filename = models.CharField(max_length=250)
    filepath = models.CharField(max_length=250)
    filesize = models.IntegerField()
    date_added = models.DateTimeField()
    user_id = models.ForeignKey(User)


class Platform(models.Model):
    name = models.CharField(max_length=100)


class Project_Platform(models.Model):
    platform_id = models.ForeignKey(Platform)
    project_id = models.ForeignKey(Project)


class Testplan(models.Model):
    project_id = models.ForeignKey(Project)
    name = models.CharField(max_length=100)
    active = models.SmallIntegerField()
    notes = models.TextField()
    author_id = models.ForeignKey(User)
    created = models.DateTimeField()


class Testplan_Platforms(models.Model):
    testplan_id = models.ForeignKey(Testplan)
    platform_id = models.ForeignKey(Platform)


class Testplan_Testcases(models.Model):
    testplan_id = models.ForeignKey(Testplan)
    testcase_id = models.ForeignKey(Testcase)
    platform_id = models.ForeignKey(Platform)
    author_id = models.ForeignKey(User, related_name="testplan_testcases_added_by")
    created = models.DateTimeField()
    assigned_id = models.ForeignKey(User, related_name="testplan_testcases_assigned_to")


class Build(models.Model):
    testplan_id = models.ForeignKey(Testplan)
    name = models.CharField(max_length=45)
    notes = models.CharField(max_length=45)
    active = models.SmallIntegerField()
    author_id = models.ForeignKey(User)
    created = models.DateTimeField()
    released = models.DateTimeField()
    closed = models.DateTimeField()


class Execution_Status(models.Model):
    status = models.CharField(max_length=45)


class TCExecution(models.Model):
    status_id = models.ForeignKey(Execution_Status)
    build_id = models.ForeignKey(Build)
    tester_id = models.ForeignKey(User)
    testplan_id = models.ForeignKey(Testplan)
    testcase_id = models.ForeignKey(Testcase)
    platform_id = models.ForeignKey(Platform)
    executed = models.DateTimeField()
    duration = models.CharField(max_length=45)
    notes = models.TextField()
