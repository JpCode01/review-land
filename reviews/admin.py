from django.contrib import admin
from reviews.models import Critico

class Criticos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao')
    list_display_links = ('id', 'nome', 'descricao')
    search_fields = ('nome',)
    list_per_page = 5
    ordering = ('nome',)

admin.site.register(Critico, Criticos)