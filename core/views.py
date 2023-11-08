from django.shortcuts import redirect, render
from .models import Login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.

def home(request):
    return render(request, "index.html")


def signup(request):

    if request.method == "POST":
        usuario = request.POST['usuario']
        nome = request.POST['nome']
        sobrenome = request.POST['sobrenome']
        email =  request.POST['email']
        senha = request.POST['senha']
        csenha = request.POST['csenha']

        myuser = User.objects.create_user(usuario, email, senha)
        myuser.first_name = nome
        myuser.last_name = sobrenome

        myuser.save()

        messages.success(request, "Sua conta foi registrada com sucesso.")

        return redirect('signin')

    return render(request, "signup.html")

def signin(request):

    if request.method == "POST":
        usuario = request.POST['usuario']
        senha = request.POST['senha']

        user = authenticate(usuario=usuario, senha=senha)

        if user is not None:
            login(request, user)
            return render(request, "index.html")

        else:
            messages.error(request, "Usuário não existente")
            return redirect('home')
    
    return render(request, "signin.html")
    

def signout(request):
    pass