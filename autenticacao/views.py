import json

from django.http import HttpResponse
from django.shortcuts import render

from .models import Cargos, Pessoa


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
    return render (request, 'listar/listar.html', {'pessoas':pessoas})

#parametro da url dinamica
def listar_unico(request):
    pessoa = Pessoa.objects.all()
    return render (request, 'listar/listar.html')


#Inserir com GET
# def listar(request):
#     if len(request.GET) != 0:
#         nome = request.GET.get('nome')
#         email = request.GET.get('email')
#         senha = request.GET.get('senha')
        
#         cargo=Cargos.objects.filter(id=1)
        
#         pessoa = Pessoa(
#             nome=nome,
#             email=email,
#             senha=senha,
#             cargo=cargo
#         )       
#     pessoas = Pessoa.objects.all()
#     return render(request, 'listar/listar.html', {'pessoas':pessoas})

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