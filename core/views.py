from django.shortcuts import redirect, render
import openai
from .models import Login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import JsonResponse


# Create your views here.
openai_api_key='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'
openai.api_key = openai_api_key


def home(request):
    return render(request, "index.html")

def ask_openai(message):
    response = openai.chat.completions.create(
        model = "gpt-4",
        messages=[
            {"role": "system", "content": "You are an helpful assistant."},
            {"role": "user", "content": message},
        ]
    )
    
    answer = response.choices[0].message.content.strip()
    return answer


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

def chat(request):
    if request.method == "POST":
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message':message,'response':response})
    return render(request, 'chat.html')


