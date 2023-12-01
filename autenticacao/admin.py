from django.contrib import admin
from .models import Pessoa, Cargos, Data, Pedido
from django_object_actions import DjangoObjectActions
from django.http import HttpResponse
# Register your models here.

class PedidoInline(admin.TabularInline):
    readonly_fields = ('nome', 'quantidade', 'descricao')
    list_display =('nome', 'quantidade', 'descricao')
    model = Pedido

@admin.register(Pessoa)
class PessoaAdmin(DjangoObjectActions, admin.ModelAdmin):
    inlines = [PedidoInline]
    list_display = (
        'foto',
        'get_nome_completo',
        'nome', 
        'sobrenome',
        'email', 
        'senha',
    )
    #readonly_fields = ('senha',)
    #search_fields = ('nome',)
    list_filter = ('cargo',)
    list_editable = ('nome', 'email','senha', 'sobrenome',)
    
    def mostra_pessoa(self, request, pessoa):
        return HttpResponse('teste')
    mostra_pessoa.label='Mostra pessoa'
    change_actions = ("mostra_pessoa",)

admin.site.register(Cargos)
admin.site.register(Data)
admin.site.register(Pedido)