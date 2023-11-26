from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from user.forms import CreateUserForm, EmailOnlyPasswordResetForm, UpdateEmailForm, UpdateUsernameForm, UpdatePasswordForm


def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account created successfully!' + user)

            return redirect('user:login')

    context = {'form': form}
    return render(request, 'register.html', context)

def user_edit(request):
    username_form = UpdateUsernameForm(instance=request.user)
    email_form = UpdateEmailForm(instance=request.user)
    password_form = UpdatePasswordForm(request.user)

    if request.method == 'POST':
        if 'username_form' in request.POST:
            username_form = UpdateUsernameForm(request.POST, instance=request.user)
            if username_form.is_valid():
                username_form.save()
                messages.success(request, 'Username updated successfully!')
                return redirect('tasks')

        elif 'email_form' in request.POST:
            email_form = UpdateEmailForm(request.POST, instance=request.user)
            if email_form.is_valid():
                email_form.save()
                messages.success(request, 'Email updated successfully!')
                return redirect('tasks')

        elif 'password_form' in request.POST:
            password_form = UpdatePasswordForm(request.user, request.POST)
            if password_form.is_valid():
                user = password_form.save(commit=False)
                user.set_password(password_form.cleaned_data['password'])
                user.save()
                messages.success(request, 'Password updated successfully!')
                return redirect('tasks')

    context = {
        'username_form': username_form,
        'email_form': email_form,
        'password_form': password_form,
    }
    return render(request, 'user_edit.html', context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('create-card')

        else:
            messages.info(request, 'Username OR password is incorrect')

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

def logout(request):
    logout(request)
    return redirect('login')