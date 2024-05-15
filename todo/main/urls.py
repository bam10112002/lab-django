from django.urls import path, include
from . import views


urlpatterns = [
    path('task/',    view=views.get_taks),
    path('project/', view=views.create_project),
    path('task/',    view=views.create_task)
]
