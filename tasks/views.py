from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required

from tasks.form import TaskForm
from tasks.models import Task
from cards.models import Card
from cards.views import get_cards_for_user


@login_required
def list_all(request):
    cards = get_cards_for_user(request.user)
    tasks = Task.objects.filter(card__in=cards)
    return render(request, 'tasks.html', {'tasks': tasks})


@login_required
def create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        card_id = request.POST.get('card')
        card = get_object_or_404(Card, id=card_id, owner=request.user)
        if form.is_valid() and card.user_has_permission(request.user, "create_task"):
            form.save()
            return redirect('tasks:list_all')
    elif request.method == "GET":
        form = TaskForm()
        return render(request, 'create_task.html', {'form': form})


@login_required
def delete(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if task.card.user_has_permission(request.user, "delete_task"):
        task.delete()
        return redirect('tasks:list_all')

    return HttpResponseForbidden("Você não tem permissão para remover esta tarefa.")


@login_required
def update(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid() and task.card.user_has_permission(request.user, "change_task"):
            form.save()
            return redirect('tasks:find_by_id', task.id)

        return HttpResponseForbidden("Você não tem permissão para atualizar esta tarefa.")

    form = TaskForm(instance=task)

    return render(request, 'update_task.html', {'form': form})


@login_required
def find_by_id(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if task.card.user_has_permission(request.user, "view_task"):
        return render(request, 'task.html', {'task': task})

    return HttpResponseForbidden("Você não tem permissão para acessar esta tarefa.")


@login_required
def complete(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if task.card.user_has_permission(request.user, "change_task"):
        task.completed = task.completed == False
        task.save()
        return redirect('cards:list_all')

    return HttpResponseForbidden("Você não tem permissão para completar esta tarefa.")
