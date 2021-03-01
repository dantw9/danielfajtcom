from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('<slug:project_slug>', views.project_page, name='project_page'),
]
