from django.contrib import admin
from usuario.models import Usuario

# Register your models here.

class Usuarios(admin.ModelAdmin):
    list_display = ('id', 'nome_completo', 'cpf', 'email',)
    list_display_links = ('id', 'nome_completo', 'cpf',)
    search_fields = ('cpf',)
    list_per_page = 15


admin.site.register(Usuario, Usuarios)