from django.shortcuts import render, redirect, render_to_response
from detest_ui.models import Project
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.contrib import auth
import logging

logger = logging.getLogger(__name__)


@login_required
def index(request):
    logger.debug("index")
    context = {'projects': Project.objects.all()}
    return render(request, 'detest_ui/index.html', context)


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


def logout_user(request):
    logout(request)
    return redirect("/login/")


def test():
    logger.debug("Hello")
