from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.listar_tarefas, name='listar_tarefas'),
    path('tasks/nova/', views.nova_tarefa, name='nova_tarefa'),
    path('tasks/editar/<int:id_tarefa>/', views.editar_tarefa, name='editar_tarefa'),
    path('tasks/excluir/<int:id_tarefa>/', views.excluir_tarefa, name='excluir_tarefa'),
    path('tasks/entregar/<int:id_tarefa>/', views.entregar_tarefa, name='entregar_tarefa'),
    path('tasks/desfazer_entrega/<int:id_tarefa>/', views.desfazer_entrega, name='desfazer_entrega'),
    path('tasks/visualizar/<int:id_tarefa>/', views.visualizar_tarefa, name='visualizar_tarefa'),
]