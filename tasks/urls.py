from django.urls import path

from tasks import views

urlpatterns = [
    path('', views.index, name='index'),
    path("listar", views.listar, name="listarTasks"),
    path('atualizar/<int:pk>', views.atualizar, name="atualizarTask"),
    path('adicionar', views.adicionar, name="adicionarTask"),
    path('deletar/<int:pk>', views.deletar, name="deletarTask"),
]

