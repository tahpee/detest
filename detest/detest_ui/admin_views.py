from django.shortcuts import render
from django.http import HttpResponseRedirect
from detest_ui import common
from detest_ui import admin_forms
from detest_ui.models import Project
from django.contrib.auth.decorators import login_required
# from django.views import generic
import logging

logger = logging.getLogger(__name__)


@login_required
def project_list(request):
    logger.debug("Admin Project List")
    context = common.default_context(request)
    return render(request, 'detest_ui/admin_projects.html', context)


@login_required
def new_project(request):
    logger.debug("Create new project")
    context = common.default_context(request)
    if request.method == 'POST':
        form = admin_forms.ProjectForm(request.POST)
        print form
        if form.is_valid():
            print "Valid Form"
            print dir(form)
            form.save()
            return HttpResponseRedirect('/admin/projects')
        else:
            print "Invalid Form"
    else:
        form = admin_forms.ProjectForm()
    context['form'] = form
    return render(request, 'detest_ui/admin_new_project.html', context)


@login_required
def project_view(request, project):
    context = common.default_context(request)
    context['project'] = Project.objects.all().filter(id=project)[0]
    return render(request, 'detest_ui/admin_project_view.html', context)


def delete_project(request):
    if request.method == 'POST':
        form = admin_forms.DeleteProjectForm(request.POST)
        if form.is_valid():
            project = Project.objects.all().filter(id=form.cleaned_data['project_id'])[0]
            print "Deleting project %s" % (project)
            project.delete()
            return HttpResponseRedirect('/admin/projects')
        else:
            return HttpResponseRedirect('/admin/projects')
    else:
        return HttpResponseRedirect('/admin/projects')
