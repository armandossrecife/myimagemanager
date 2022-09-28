from django.contrib import admin
from myimages.models import Imagem

class Imagens(admin.ModelAdmin):
    list_display = ('id', 'nome', 'foto')
    list_display_links = ('nome',)
    search_fields = ('nome',)

admin.site.register(Imagem, Imagens)