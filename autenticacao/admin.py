from django.contrib import admin
from .models import Pessoa, Cargos, Data
# Register your models here.

@amin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):

admin.site.register(Cargos)
admin.site.register(Data)