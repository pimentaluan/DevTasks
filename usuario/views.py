from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

def login_view(request):
    if request.method == 'POST': 
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            authenticated_user = authenticate(request, username=user.username, password=password)
            if authenticated_user is not None:
                login(request, authenticated_user)
                return redirect('/tasks/')
            else:
                messages.error(request, 'Email ou senha inválidos.')
        except User.DoesNotExist:
            messages.error(request, 'Email não encontrado.')

    return render(request, 'usuario/login.html')

def registrar(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        username = email.split('@')[0]

        if password == password2:
            user = User.objects.create_user(username=username,email=email, password=password)
            user.save()
            return redirect('')
        else:
            messages.error(request, 'Senhas não conferem.')
            
    return render(request, 'usuario/registrar.html')

def logout(request):
    logout(request)
    return redirect('login')