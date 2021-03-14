from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:project_slug>', views.project_page, name='project_page'),
]
