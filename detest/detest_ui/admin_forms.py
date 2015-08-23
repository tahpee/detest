from detest_ui import models
from django.forms import ModelForm
from django import forms


class ProjectForm(ModelForm):
    class Meta:
        model = models.Project
        fields = ['name', 'prefix', 'active', 'public', 'notes']

class DeleteProjectForm(forms.Form):
    project_id = forms.IntegerField(label="Project ID")

