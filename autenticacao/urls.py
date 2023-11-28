from django.urls import path, include
from autenticacao import views

urlpatterns = [
    path('cadastro/', views.cadastro ),
]