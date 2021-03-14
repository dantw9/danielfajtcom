from django.shortcuts import render
from django.http import Http404
from django.template import TemplateDoesNotExist
import os
import json


def index(request):
    # Read projects data from json file
    with open(os.path.join(os.path.dirname(__file__), "projects.json"), 'r', encoding='utf-8') as f:
        projects = json.load(f)

    context = {'projects': projects}
    return render(request, 'projects/index.html', context)


def project_page(request, project_slug):
    try:
        template_name = 'projects/' + project_slug + '.html'
        print('template_name', template_name)
        return render(request, template_name)
    except TemplateDoesNotExist:
        raise Http404(f'Project "{project_slug}" not found')
