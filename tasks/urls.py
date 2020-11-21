from django.urls import path
from . import views
from .views import TaskCreate, TaskList, TaskDelete, TaskUpdate

urlpatterns = [
    path("", views.index, name="index"),
    path('listar', TaskList.as_view()),
    path('adicionar', TaskCreate.as_view()),
    path('atualizar/<int:pk>', TaskUpdate.as_view()),
    path('deletar/<int:pk>', TaskDelete.as_view())
]
