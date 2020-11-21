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
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    return HttpResponse("Task created succesfully")

class TaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
     _json = serializers.serialize("json", queryset)
    return HttpResponse(_json, content_type="application/json")

class TaskUpdate(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    return HttpResponse("Task updated succesfully")

class TaskDelete(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer 
    return HttpResponse("Task deleted succesfully")
