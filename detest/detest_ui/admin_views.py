from django.shortcuts import render
from detest_ui import common
from django.contrib.auth.decorators import login_required
import logging

logger = logging.getLogger(__name__)


@login_required
def project_list(request):
    logger.debug("Admin Project List")
    context = common.default_context(request)
    return render(request, 'detest_ui/admin_projects.html', context)
