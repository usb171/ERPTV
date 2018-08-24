from django.contrib import admin
from .models import Profile, Funcao

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['nomeCompleto', 'funcao', 'matricula', 'dataAdmissao']
    readonly_fields = ['acesso']

class FuncaoAdmin(admin.ModelAdmin):
    list_display = ['nome']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Funcao, FuncaoAdmin)
