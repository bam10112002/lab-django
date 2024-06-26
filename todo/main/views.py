from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer

@api_view(['GET', "POST"])
def task(request):
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        query = request.GET.get('q')

        if request.GET.get('q'):
            tasks = Task.objects.filter(title__icontains=query) | Task.objects.filter(description__icontains=query)
        else:
            tasks = Task.objects.all()

        task_data = [{'title': task.title, 'description': task.description, 'project': task.project.title} for task in tasks]
        return HttpResponse(JsonResponse({'tasks': task_data}))

@api_view(['GET','POST'])
def project(request):
    if request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "GET":
        query = request.GET.get('q')

        if request.GET.get('q'):
            projects = Project.objects.filter(title__icontains=query)
        else:
            projects = Project.objects.all()

        project_data = [{'title': project.title} for project in projects]
        return HttpResponse(JsonResponse({'projects': project_data}))
    