from django.shortcuts import render

def register(request):
    return render(request, 'cadastro.html')

def login(request):
    return render(request, 'login.html')