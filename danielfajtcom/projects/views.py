from django.shortcuts import render
from django.views.generic import ListView
from django.http import Http404
from django.template import TemplateDoesNotExist
from . import models
from main import models as main_models
from datetime import datetime


class Index(ListView):
    model = models.ProjectModel
    template_name = 'projects/index.html'
    context_object_name = 'projects'


def project_page(request, project_slug):
    context = {}

    try:
        template_name = 'projects/' + project_slug + '.html'
        return render(request, template_name, context)
    except TemplateDoesNotExist:
        raise Http404(f'Project "{project_slug}" not found')
