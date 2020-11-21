from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from tasks.models import Task
from django.core import serializers
from django.forms.models import model_to_dict
from rest_framework import generics
from rest_framework.response import Response
from tasks.serializer import TaskSerializer


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")

class TaskCreate(generics.CreateAPIView):
    data = JSONParser().parse(request)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer(data=data)
    def create(request):
        if serializer_class.is_valid():
            return JsonResponse(taskSerializer.data, status=201)
        return JsonResponse(taskSerializer.errors, status=400)
        
class TaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskUpdate(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer   

class TaskDelete(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer   
