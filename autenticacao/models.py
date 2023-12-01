from django.db import models
from django.utils.safestring import mark_safe


class Cargos(models.Model):
    nome = models.CharField(max_length=20)
    def __str__(self):
        return self.nome


class Pessoa(models.Model):
    foto = models.ImageField(upload_to = "foto")
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=100)
    cargo = models.ManyToManyField(Cargos)

    def __str__(self):
        return self.nome
    
    #criando método para pegar nome e sobrenome
    def get_nome_completo(self):
        return f"{self.nome} {self.sobrenome}"
    
    #mostrar foto
    @mark_safe
    def foto(self):
        return f"<img width='60px' src='/media/{self.foto}'>"

class Data(models.Model):
    data = models.DateTimeField()

class Pedido(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    descricao = models.TextField()
    pessoa = models.ForeignKey(Pessoa, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.nome