from django.urls import path

from tasks import views

urlpatterns = [
    path("listar", views.getList, name="AllTasks"),
    path('atualizar/<int:pk>', views.updateTask, name="ChangeTask"),
    path('adicionar', views.createTask, name="createTask"),
    path('deletar', views.delete_all, name="deleteTask"),
]

