import folium
import json

from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime
from .models import Pokemon, PokemonEntity




MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons = Pokemon.objects.all()
    now_local = localtime()

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in pokemons:
        for pokemon_entity in pokemon.entities.filter(disappeared_at__gt=now_local,appearance_at__lt=now_local):
            add_pokemon(
                folium_map, pokemon_entity.lat,
                pokemon_entity.lon,
                request.build_absolute_uri(pokemon.img.url)
            )


    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': request.build_absolute_uri(pokemon.img.url),
            'title_ru': pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    now_local = localtime()
    pokemon = get_object_or_404(Pokemon,pk=pokemon_id)

    requested_pokemon = pokemon
    next_evolutions = pokemon.next_evolutions.first()
    pokemon_data = {
        "title_ru": pokemon.title,
        'img_url': pokemon.img.url,
        "title_en": pokemon.title_en,
        "title_jp": pokemon.title_jp,
        "description":pokemon.description,
        "next_evolution": {
            "title_ru": pokemon.previous_evolution.title,
            "pokemon_id":pokemon.previous_evolution.pk,
            "img_url": pokemon.previous_evolution.img.url
        } if pokemon.previous_evolution else None,
        "previous_evolution": {
            "title_ru": next_evolutions.title,
            "pokemon_id": next_evolutions.pk,
            "img_url": next_evolutions.img.url
        } if next_evolutions else None
    }


    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in requested_pokemon.entities.filter(disappeared_at__gt=now_local,appearance_at__lt=now_local):
            add_pokemon(
                folium_map, pokemon_entity.lat,
                pokemon_entity.lon,
                request.build_absolute_uri(requested_pokemon.img.url)
            )


    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon_data
    })
