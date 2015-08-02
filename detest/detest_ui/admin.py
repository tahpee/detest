from django.contrib import admin
from detest_ui.models import Project, Testsuite, TCPriority, TCStatus, TCExecution_Type, Testcase

# Register your models here.

admin.site.register(Project)
admin.site.register(Testsuite)
admin.site.register(TCPriority)
admin.site.register(TCStatus)
admin.site.register(TCExecution_Type)
admin.site.register(Testcase)
