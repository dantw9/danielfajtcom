from django.shortcuts import render
from django.views.generic import ListView
from django.http import Http404
from django.template import TemplateDoesNotExist
from . import models


class Index(ListView):
    model = models.ProjectModel
    template_name = 'projects/index.html'
    context_object_name = 'projects'


def project_page(request, project_slug):
    photos = [
        'https://picsum.photos/1600/1800?random=1',
        'https://picsum.photos/200/300?random=2',
        'https://picsum.photos/200/300?random=3',
        'https://picsum.photos/200/300?random=4',
        'https://picsum.photos/200/300?random=5',
        '/static/images/projects.olab.png'
    ]

    context = {'photos': photos}

    try:
        template_name = 'projects/' + project_slug + '.html'
        return render(request, template_name, context)
    except TemplateDoesNotExist:
        raise Http404(f'Project "{project_slug}" not found')
