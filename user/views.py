from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from user.forms import CreateUserForm, EmailOnlyPasswordResetForm


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


def reset_password(request):
    if request.method == "POST":
        form = EmailOnlyPasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            generate_new_password(email)
            return HttpResponse('Password updated successfully.')

        return HttpResponse('Invalid request.')

    form = EmailOnlyPasswordResetForm()
    context = {'form': form}
    return render(request, 'reset_password.html', context)


def generate_new_password(email):
    user = get_object_or_404(User, email=email)
    new_password = User.objects.make_random_password()
    user.password = make_password(new_password)
    user.save()

    send_mail(
        'Password Update',
        f'Your password has been updated. Your new password is: {new_password}',
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
