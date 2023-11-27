from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from user.forms import CreateUserForm, EditPasswordForm, EditUserForm, EmailOnlyPasswordResetForm


def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account created successfully! ' + user)

            return redirect('user:login')

    context = {'form': form}
    return render(request, 'register.html', context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('cards:list_all')

        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'login.html', context)

@login_required()
def logout(request):
    auth_logout(request)
    return redirect('user:login')
    

@login_required()
def user_edit(request):
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User information updated successfully!')
            return redirect('cards:list_all')
        
    else:
        form = EditUserForm(instance=request.user)
    
    context = {'form':form}
    return render(request, 'user_edit.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = EditPasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Sua senha foi alterada com sucesso!')
            return redirect('cards:list_all')
    else:
        form = EditPasswordForm(request.user)

    return render(request, 'change_password.html', {'form': form}) 


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