from django.shortcuts import render, redirect, render_to_response
from detest_ui.models import Project
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.contrib import auth
from django.views import generic
import logging

logger = logging.getLogger(__name__)


def default_context(request, project=None):
    context = {'projects': Project.objects.all().order_by('name')}
    request.session['current_project'] = project
    if project in [x.name for x in context['projects']]:
        request.session['current_project'] = project
    else:
        request.session['current_project'] = Project.objects.all().order_by('name')[0].name
    context['current_project'] = request.session['current_project']
    return context


@login_required
def index(request):
    logger.debug("index")
    context = default_context(request)
    return render(request, 'detest_ui/index.html', context)

# @login_required
# def dashboard(request, project=None):
    # context = default_context(request,

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
