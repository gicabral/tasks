from django.urls import path
from . import views
from .views import TaskCreate, TaskList, TaskDelete, TaskUpdate

urlpatterns = [
    path("", views.index, name="index"),
    path("list", views.getTasks, name="AllTasks"),
    path("<int:task_id>", views.getTask, name="SingleTask"),
    path("create", views.createTask, name="CreateTask"),
    path("delete/<int:task_id>", views.deleteTask, name="DeleteTask"),
    path("deleteAll", views.deleteTasks, name="DeleteAllTask"),
    path("update/<int:task_id>", views.updateTask, name="UpdateTask"),
]
