from django.shortcuts import redirect, render, get_object_or_404

from tasks.form import TaskForm
from tasks.models import Task

def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {'tasks': tasks})

def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:list_tasks')
    elif request.method == "GET":
        form = TaskForm()
        return render(request, 'create_task.html', {'form': form})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('tasks:list_tasks')

def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:find_task_by_id', task.id)

    form = TaskForm(instance=task)

    return render(request, 'update_task.html', {'form': form})

def find_task_by_id(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task.html', {'task': task})

def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = task.completed == False
    task.save()
    return redirect('tasks:list_tasks')
