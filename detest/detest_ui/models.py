from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=45)
    notes = models.TextField(default="")
    prefix = models.CharField(max_length=45)
    active = models.BooleanField(default=True)
    public = models.BooleanField(default=False)

    def __str__(self):
        return "%s: %s" % (self.prefix, self.name)


class Testsuite(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()
    project = models.ForeignKey(Project)

    def __str__(self):
        return "%s" % (self.name)


class Testsuite_CT(models.Model):
    parent = models.ForeignKey(Testsuite, related_name="parent_testsuite")
    child = models.ForeignKey(Testsuite, related_name="child_testsuite")


class TCPriority(models.Model):
    priority = models.CharField(max_length=45)

    def __str__(self):
        return "%d: %s" % (self.id, self.priority)


class TCStatus(models.Model):
    status = models.CharField(max_length=45)

    def __str__(self):
        return "%d: %s" % (self.id, self.status)


class TCExecution_Type(models.Model):
    execution_type = models.CharField(max_length=45)

    def __str__(self):
        return "%d: %s" % (self.id, self.execution_type)


class Testcase(models.Model):
    external_id = models.IntegerField()
    testsuite = models.ForeignKey(Testsuite)
    version = models.IntegerField()
    name = models.CharField(max_length=100)
    summary = models.TextField(null=True)
    preconditions = models.TextField(null=True)
    tcpriority = models.ForeignKey(TCPriority)
    tcstatus = models.ForeignKey(TCStatus)
    tcexecution_type = models.ForeignKey(TCExecution_Type)
    author = models.ForeignKey(User, related_name="testcase_authored_by")
    modified_by = models.ForeignKey(User, null=True, related_name="testcase_modified_by")
    created = models.DateTimeField()
    modified = models.DateTimeField(null=True)
    previous_version = models.ForeignKey('self', null=True)
    requirement = models.CharField(max_length=100)
    estimate = models.IntegerField(null=True)

    def __str__(self):
        return "%d (%d): %s->%s" % (self.external_id, self.id, self.testsuite, self.name)


class Teststep(models.Model):
    step_number = models.IntegerField()
    actions = models.TextField()
    expected_results = models.TextField()


class TCAttachment(models.Model):
    testcase = models.ForeignKey(Testcase)
    title = models.CharField(max_length=250)
    filename = models.CharField(max_length=250)
    filepath = models.CharField(max_length=250)
    filesize = models.IntegerField()
    date_added = models.DateTimeField()
    user = models.ForeignKey(User)


class Platform(models.Model):
    name = models.CharField(max_length=100)


class Project_Platform(models.Model):
    platform = models.ForeignKey(Platform)
    project = models.ForeignKey(Project)


class Testplan(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=100)
    active = models.SmallIntegerField()
    notes = models.TextField()
    author = models.ForeignKey(User)
    created = models.DateTimeField()


class Testplan_Platforms(models.Model):
    testplan = models.ForeignKey(Testplan)
    platform = models.ForeignKey(Platform)


class Testplan_Testcases(models.Model):
    testplan = models.ForeignKey(Testplan)
    testcase = models.ForeignKey(Testcase)
    platform = models.ForeignKey(Platform)
    author = models.ForeignKey(User, related_name="testplan_testcases_added_by")
    created = models.DateTimeField()
    assigned = models.ForeignKey(User, related_name="testplan_testcases_assigned_to")


class Build(models.Model):
    testplan = models.ForeignKey(Testplan)
    name = models.CharField(max_length=45)
    notes = models.CharField(max_length=45)
    active = models.SmallIntegerField()
    author = models.ForeignKey(User)
    created = models.DateTimeField()
    released = models.DateTimeField()
    closed = models.DateTimeField()


class Execution_Status(models.Model):
    status = models.CharField(max_length=45)


class TCExecution(models.Model):
    status = models.ForeignKey(Execution_Status)
    build = models.ForeignKey(Build)
    tester = models.ForeignKey(User)
    testplan = models.ForeignKey(Testplan)
    testcase = models.ForeignKey(Testcase)
    platform = models.ForeignKey(Platform)
    executed = models.DateTimeField()
    duration = models.CharField(max_length=45)
    notes = models.TextField()
