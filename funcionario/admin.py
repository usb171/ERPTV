from django.contrib import admin
from .models import Funcionario, Funcao

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['nomeCompleto', 'funcao', 'matricula', 'dataAdmissao']
    readonly_fields = ['acesso']

    search_fields = (
        'nomeCompleto',
    )



class FuncaoAdmin(admin.ModelAdmin):
    list_display = ['nome']

    search_fields = (
        'nome',
    )


admin.site.register(Funcionario, ProfileAdmin)
admin.site.register(Funcao, FuncaoAdmin)
