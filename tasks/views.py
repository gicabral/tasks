from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from tasks.models import Task
from django.core import serializers
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from tasks.serializer import TaskSerializer


# Create your views here.


@api_view(["GET"])
def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")


@api_view(["GET"])
def getTasks(request):
    allTasks = Task.objects.all()

    _json = serializers.serialize("json", allTasks)
    # return
    return HttpResponse(_json, content_type="application/json")


@api_view(["GET"])
def getTask(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
        return JsonResponse(model_to_dict(task), safe=False)
    except Task.DoesNotExist:
        raise Http404("Task does not exist")


@api_view(["POST"])
def createTask(request):
    data = JSONParser().parse(request)
    taskSerializer = TaskSerializer(data=data)
    if taskSerializer.is_valid():
        taskSerializer.save()
        return JsonResponse(taskSerializer.data, status=201)
    return JsonResponse(taskSerializer.errors, status=400)


@api_view(["PUT"])
def updateTask(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except:
        raise Http404("Task does not exist")

    # print(task["title"])
    data = JSONParser().parse(request)
    print("title" in data)
    if "title" in data:
        task.title = data["title"]
    if "pub_date" in data:
        task.pub_date = data["pub_date"]
    if "description" in data:
        task.description = data["description"]

    task.save()

    return JsonResponse(model_to_dict(task), status=201, safe=False)


@api_view(["DELETE"])
def deleteTask(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
        task.delete()
    except Task.DoesNotExist:
        raise Http404("Task does not exist")
    return HttpResponse("Task deleted succesfully")


@api_view(["DELETE"])
def deleteTasks(request):
    task = Task.objects.all().delete()
    return HttpResponse("All tasks deleted succesfully") 