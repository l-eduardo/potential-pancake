from django.shortcuts import redirect, render

from tasks.form import TaskForm
from tasks.models.task import Task

def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {'tasks': tasks})

def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_tasks')
    elif request.method == "GET":
        form = TaskForm()
        return render(request, 'create_task.html', {'form': form})

def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('list_tasks')

def complete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.completed = task.completed == False
    task.save()
    return redirect('list_tasks')