from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from tasks.models import Tasks

def listar_tarefas(request):
    tasks = Tasks.objects.filter(autor=request.user).order_by('-data_entrega')
    return render(request, 'tasks/listar_tarefas.html', {'tarefas': tasks})

def nova_tarefa(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        data_entrega = request.POST.get('data_entrega')
        arquivo = request.FILES.get('arquivo')

        task = Tasks(autor=request.user, titulo=titulo, descricao=descricao, data_entrega=data_entrega, arquivo=arquivo)
        task.save()

        return redirect('/tasks/')
    return render(request, 'tasks/nova_tarefa.html')

def editar_tarefa(request, id_tarefa):
    task = Tasks.objects.get(id=id_tarefa)
    if request.method == 'POST':
        task.titulo = request.POST.get('titulo')
        task.descricao = request.POST.get('descricao')
        task.data_entrega = request.POST.get('data_entrega')
        task.arquivo = request.FILES.get('arquivo')
        task.save()
        return redirect('/tasks/')
    return render(request, 'tasks/editar_tarefa.html', {'task': task})


def excluir_tarefa(request, id_tarefa):
    task = Tasks.objects.get(id=id_tarefa)
    task.delete()
    return redirect('/tasks/')

def entregar_tarefa(request, id_tarefa):
    task = Tasks.objects.get(id=id_tarefa)
    task.entregue = True
    task.save()
    return redirect('/tasks/')

def desfazer_entrega(request, id_tarefa):
    task = Tasks.objects.get(id=id_tarefa)
    task.entregue = False
    task.save()
    return redirect('/tasks/')

def visualizar_tarefa(request, id_tarefa):
    task = Tasks.objects.get(id=id_tarefa)
    return render(request, 'tasks/visualizar_tarefa.html', {'task': task})
