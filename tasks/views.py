from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from tasks.form import TaskForm
from tasks.models import Task
from cards.models import Card
from cards.views import get_cards_for_user


@login_required
def list_all(request):
    """
    Lista todas as tarefas associadas aos cards que o usuário logado tem acesso.

    Args:
        request (HttpRequest): O objeto de solicitação Django.

    Returns:
        HttpResponse: Uma resposta HTTP que renderiza a página com todas as tarefas associadas ao usuário.
    """
    cards = get_cards_for_user(request.user)
    tasks = Task.objects.filter(card__in=cards)
    return render(request, 'tasks.html', {'tasks': tasks})


@login_required
def create(request):
    """
    Cria uma nova tarefa se o usuário tiver acesso ao card que ela pertence e permissão para criar.

    Args:
        request (HttpRequest): O objeto de solicitação Django.

    Returns:
        HttpResponse: Uma resposta HTTP redirecionando para a lista de tarefas ou exibindo um erro se a criação falhar.
    """
    if request.method == 'POST':
        form = TaskForm(request.POST)
        card_id = request.POST.get('card')
        card = Card.objects.get(id=card_id)
        if form.is_valid() and card.user_has_permission(request.user, 'add_task'):
            form.save()
            return redirect('cards:list_all')
        return HttpResponseForbidden('Você não tem permissão para criar tarefas neste card.')
    elif request.method == 'GET':
        form = TaskForm()
        return render(request, 'create_task.html', {'form': form})


@login_required
def delete(request, pk):
    """
    Remove uma tarefa se o usuário tiver acesso ao card que ela pertence e permissão para remover.

    Args:
        request (HttpRequest): O objeto de solicitação Django.
        pk (int): A chave primária da tarefa.

    Returns:
        HttpResponse: Uma resposta HTTP redirecionando para a lista de tarefas ou exibindo um erro se a exclusão falhar.
    """
    task = Task.objects.get(pk=pk)

    if task.card.user_has_permission(request.user, 'delete_task'):
        task.delete()
        return redirect('cards:list_all')

    return HttpResponseForbidden('Você não tem permissão para remover esta tarefa.')


@login_required
def update(request, pk):
    """
    Atualiza uma tarefa se o usuário tiver acesso ao card que ela pertence e permissão para atualizar.

    Args:
        request (HttpRequest): O objeto de solicitação Django.
        pk (int): A chave primária da tarefa.

    Returns:
        HttpResponse: Uma resposta HTTP redirecionando para a página da tarefa atualizada ou exibindo um erro se a atualização falhar.
    """
    task = Task.objects.get(pk=pk)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid() and task.card.user_has_permission(request.user, 'change_task'):
            form.save()
            return redirect('tasks:find_by_id', task.id)

        return HttpResponseForbidden('Você não tem permissão para atualizar esta tarefa.')

    form = TaskForm(instance=task)

    return render(request, 'update_task.html', {'form': form})


@login_required
def find_by_id(request, pk):
    """
    Visualiza uma tarefa específica.

    Args:
        request (HttpRequest): O objeto de solicitação Django.
        pk (int): A chave primária da tarefa.

    Returns:
        HttpResponse: Uma resposta HTTP que renderiza a página da tarefa ou exibe um erro se o acesso for negado.
    """
    task = Task.objects.get(pk=pk)

    if task.card.user_has_permission(request.user, 'view_task'):
        return render(request, 'task.html', {'task': task})

    return HttpResponseForbidden('Você não tem permissão para acessar esta tarefa.')


@login_required
def complete(request, pk):
    """
    Marca uma tarefa como concluída ou não concluída.

    Args:
        request (HttpRequest): O objeto de solicitação Django.
        pk (int): A chave primária da tarefa.

    Returns:
        HttpResponse: Uma resposta HTTP redirecionando para a lista de tarefas ou exibindo um erro se a ação falhar.
    """
    task = Task.objects.get(pk=pk)

    if task.card.user_has_permission(request.user, 'change_task'):
        task.completed = task.completed == False
        task.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))

    return HttpResponseForbidden('Você não tem permissão para completar esta tarefa.')


@login_required
def create_task_to_card(request, pk):
    """
    Cria uma nova tarefa associada a um determinado card.

    Args:
        request (HttpRequest): O objeto de solicitação Django.
        pk (int): A chave primária do card.

    Returns:
        HttpResponse: Uma resposta HTTP que renderiza o formulário para criar uma nova tarefa associada ao card.
    """
    if request.method == 'GET':
        form = TaskForm()
        form.fields['card'].initial = pk
        return render(request, 'create_task.html', {'form': form})
