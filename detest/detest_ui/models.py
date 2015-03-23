from django.db import models


# Create your models here.
class Project(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    notes = models.TextField(null=True)
    color = models.CharField(max_length=12)
    active = models.IntegerField(default=1)
    prefix = models.CharField(max_length=16)
    tc_counter = models.IntegerField(default=0)
    is_public = models.IntegerField(default=1)
    options = models.TextField()

    def __str__(self):
        return "%s (%d)" % (self.name, self.id)
