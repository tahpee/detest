from django.shortcuts import render, redirect, render_to_response
from detest_ui.models import Project, Testsuite
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.contrib import auth
from django.views import generic
import logging

logger = logging.getLogger(__name__)


def default_context(request, project=None):
    context = {'projects': Project.objects.all().order_by('name')}
    if project is not None and project in [x.name for x in context['projects']]:
        context['current_project'] = project
    else:
        context['current_project'] = request.session.get('current_project', None)
        if context['current_project'] is None:
            context['current_project'] = Project.objects.all().order_by('name')[0].name
    print "2: context['current_project'] = %s" % (context['current_project'])
    return context


def project_testsuites(project_name):
    print "project_testsuites::project_name = %s" % (project_name)
    testsuites = Testsuite.objects.all().order_by('name').filter(project__name=project_name)
    print testsuites[0].project
    return testsuites


@login_required
def index(request):
    logger.debug("index")
    context = default_context(request)
    return render(request, 'detest_ui/index.html', context)


@login_required
def design_top(request, project):
    context = default_context(request, project)
    context['testsuites'] = project_testsuites(context['current_project'])
    print context
    return render(request, 'detest_ui/design_top.html', context)


@login_required
def dashboard(request, project=None):
    context = default_context(request, project)
    return render(request, 'detest_ui/project_dashboard.html', context)


@login_required
def project(request, project):
    context = default_context(request, project)
    return render(request, 'detest_ui/project_dashboard.html', context)


@login_required
def project_list(request):
    logger.debug("Project List")
    context = default_context(request)
    return render(request, 'detest_ui/projects.html', context)


def buttons(request):
    logger.debug("buttons")
    # context = {'projects': Project.objects.all()}
    return render(request, 'detest_ui/buttons.html')


def login_view(request):
    context = {}
    context.update(csrf(request))
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    logger.debug("Username = %s" % (username))
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            logger.debug("Successful login for user %s" % (username))
            return redirect('/')
        else:
            # Account is disabled
            # TODO: Create a disabled page
            logger.debug("Account disabled for user %s" % (username))
            pass
    else:
        # Login Failed
        logger.debug("Login failed for user %s" % (username))
        context['username'] = username
        return render_to_response('detest_ui/login.html', context)


@login_required
def project_view(request, project):
    context = default_context(request)
    return render(request, 'detest_ui/project.html', context)


class ProjectView(generic.DetailView):
    model = Project
    template_name = 'detest_ui/project_view.html'
