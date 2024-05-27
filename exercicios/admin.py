from django.contrib import admin
from exercicios.models import Exercicio

# Register your models here.

class Exercicios(admin.ModelAdmin):
    list_display = ('uuid', 'nome', 'repeticoes', 'descricao')
    list_display_links = ('uuid', 'nome')
    search_fields = ('uuid',)
    list_per_page = 15


admin.site.register(Exercicio, Exercicios)