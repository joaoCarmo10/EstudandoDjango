from django.urls import path, include
from autenticacao import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro' ),
    path('listar', views.listar, name='listar')
    #path('valida_formulario', views.valida_formulario, name='valida_formulario'),
]