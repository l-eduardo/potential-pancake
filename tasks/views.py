from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404

from tasks.form import TaskForm
from tasks.models import Task


def list_all(request):
    tasks = get_list_or_404(Task)
    return render(request, 'tasks.html', {'tasks': tasks})


def create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:list_all')
    elif request.method == "GET":
        form = TaskForm()
        return render(request, 'create_task.html', {'form': form})


def delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('tasks:list_all')


def update(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:find_by_id', task.id)

    form = TaskForm(instance=task)

    return render(request, 'update_task.html', {'form': form})


def find_by_id(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task.html', {'task': task})


def complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = task.completed == False
    task.save()
    return redirect('tasks:list_all')
