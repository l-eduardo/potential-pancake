from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CreateUserForm


def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Conta criada com sucesso! ' + user)

            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


def user_login(request):  # nome antigo era 'login', ver depois se não vai implicar em outras partes do sistema

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('tasks:list_all')

        else:
            messages.info(request, 'Usuário OU senha estão incorretos')

    context = {}
    return render(request, 'login.html', context)

@login_required
def user_edit(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Informações do usuário atualizadas com sucesso!')
            return redirect('tasks')
        
    else:
        form = CreateUserForm(instance=request.user)
    
    context = {'form':form}
    return render(request, 'user_edit.html', context)
