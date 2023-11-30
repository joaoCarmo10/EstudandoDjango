from django.contrib import admin
from .models import Pessoa, Cargos, Data, Pedido
# Register your models here.

class Pedido

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = (
        'nome', 
        'email', 
        'senha',
    )
    #readonly_fields = ('senha',)
    search_fields = ('nome',)
    list_filter = ('cargo',)
    list_editable = ('email','senha')

admin.site.register(Cargos)
admin.site.register(Data)
admin.site.register(Pedido)