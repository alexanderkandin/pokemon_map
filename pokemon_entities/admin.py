from django.contrib import admin
from .models import Pokemon, PokemonEntity

class PokemonAdmin(admin.ModelAdmin):
    list_display = ("title","id")

class PokemonEntityAdmin(admin.ModelAdmin):
    list_display = ("pokemon", "lat",'lon','appearance_at',"disappeared_at")

admin.site.register(Pokemon,PokemonAdmin)
admin.site.register(PokemonEntity,PokemonEntityAdmin)