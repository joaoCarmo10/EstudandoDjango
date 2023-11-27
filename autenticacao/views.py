from django.shortcuts import render
from django.http import HttpResponse

def cadastro(requests):
    return HttpResponse('Faça seu cadastro')

def auth(request):
    return HttpResponse('você está na autenticação')
