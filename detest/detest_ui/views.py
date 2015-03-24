from django.shortcuts import render
from detest_ui.models import Project


def index(request):
    context = {'projects': Project.objects.all()}
    return render(request, 'detest_ui/index.html', context)
