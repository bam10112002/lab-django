from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer

@api_view(['GET'])
def get_taks(request):
    query = request.GET.get('q')

    if request.GET.get('q'):
        tasks = Task.objects.filter(title__icontains=query) | Task.objects.filter(description__icontains=query)
    else:
        tasks = Task.objects.all()

    task_data = [{'title': task.title, 'description': task.description, 'project': task.project.title} for task in tasks]
    return HttpResponse(JsonResponse({'tasks': task_data}))

@api_view(['POST'])
def create_project(request):
    if request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_task(request):
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
