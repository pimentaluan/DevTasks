from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages

def login(request):
    if request.method == 'POST': 
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/tasks/')
        else:
            messages.error(request, 'Email ou senha inválidos.')
    return render(request, 'usuario/login.html')

def registrar(request):
    return render(request, 'usuario/registrar.html')

def logout(request):
    return render(request, 'usuario/logout.html')