from django.urls import path, include
from . import views


urlpatterns = [
    path('task/',    view=views.task),
    path('project/', view=views.project),
]
