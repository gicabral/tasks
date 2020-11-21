from django.urls import path

from tasks import views

urlpatterns = [
    path('', views.index, name='index'),
    path("listar", views.getList, name="AllTasks"),
    path('atualizar/<int:pk>', views.updateTask, name="ChangeTask"),
    path('adicionar', views.createTask, name="createTask"),
    path('deletar/<int:pk>', views.delete_all, name="deleteTask"),
]

