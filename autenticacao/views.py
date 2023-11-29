from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Pessoa

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro/index.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        pessoa = Pessoa(
            nome = nome, 
            email = email, 
            senha = senha
        )
        pessoa.save()
        return HttpResponse('Você foi cadastrado!')

def listar(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'listar.html', {'pessoas':pessoas})

# Buscando todos os dados
# def listar(request):
#     pessoas = Pessoa.objects.filter(nome='Osiris')
#     return render(request, 'listar.html', {'pessoas':pessoas})

#Operador E
# def listar(request):
#     pessoas = Pessoa.objects.filter(nome='Osiris').filter(email='osiris@gmail.com')
#     return render(request, 'listar.html', {'pessoas':pessoas})

#Operador OR
# def listar(request):
#     pessoas = Pessoa.objects.filter(nome='Osiris') | Pessoa.objects.filter(email='cruzeiro@gmail.com')
#     return render(request, 'listar.html', {'pessoas':pessoas})