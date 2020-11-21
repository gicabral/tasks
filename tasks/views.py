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
     def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.DATA, files=request.FILES)

        if serializer.is_valid():
            self.pre_save(serializer.object)
            self.object = serializer.save(force_insert=True)
            self.post_save(self.object, created=True)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED,
                            headers=headers)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class TaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskUpdate(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer   

class TaskDelete(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer   
