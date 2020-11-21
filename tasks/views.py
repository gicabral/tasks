from django.shortcuts import render
from django.http import HttpResponse
from tasks.serializer import TaskSerializer
from tasks.models import Task 
from rest_framework import generics
from django.core import serializers
import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response


@api_view(["GET"])
def getList(request):
    task = Task.objects.all()
    SomeModel_json = serializers.serialize("json", task)
    return HttpResponse(SomeModel_json, content_type="application/json")

@api_view(["POST"])
def createTask(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

@api_view(["PUT"])
def updateTask(request, pk):
    try:
        task = Task.objects.get(pk = pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TaskSerializer(task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def delete_all(request):
    try:
        task = Task.objects.all()
        task.delete()
        return HttpResponse("task deleted", content_type="application/json")
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
