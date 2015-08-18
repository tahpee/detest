from detest_ui.models import Project
import logging

logger = logging.getLogger(__name__)


def default_context(request, project=None):
    context = {'projects': Project.objects.all().order_by('name')}
    context['user_is_admin'] = request.user.is_superuser
    if project is not None and project in [x.name for x in context['projects']]:
        context['current_project'] = project
    else:
        context['current_project'] = request.session.get('current_project', None)
        if context['current_project'] is None:
            if len(Project.objects.all()) > 0:
                context['current_project'] = Project.objects.all().order_by('name')[0].name
            else:
                context['current_project'] = None
    return context
