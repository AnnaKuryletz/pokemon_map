import folium
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Pokemon, PokemonEntity
from django.utils.timezone import localtime

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision"
    "/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832"
    "&fill=transparent"
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
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    local_time = localtime()

    pokemon_entities = PokemonEntity.objects.filter(
        disappeared_at__gt=local_time, appeared_at__lt=local_time
    )

    for entity in pokemon_entities:
        pokemon = entity.pokemon
        img_url = request.build_absolute_uri(pokemon.image.url) if pokemon.image else ""
        add_pokemon(folium_map, entity.lat, entity.lon, img_url)

    pokemons = Pokemon.objects.all()

    pokemons_on_page = []

    for pokemon in pokemons:
        img_url = request.build_absolute_uri(pokemon.image.url) if pokemon.image else ""
        pokemons_on_page.append(
            {
                "pokemon_id": pokemon.id,
                "img_url": img_url,
                "title_ru": pokemon.title_ru,
            }
        )

    return render(
        request,
        "mainpage.html",
        context={
            "map": folium_map._repr_html_(),
            "pokemons": pokemons_on_page,
        },
    )


def show_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)

    img_url = request.build_absolute_uri(pokemon.image.url) if pokemon.image else ""

    pokemon_page = {
        "pokemon_id": pokemon.id,
        "title_ru": pokemon.title_ru,
        "title_en": pokemon.title_en,
        "title_jp": pokemon.title_jp,
        "img_url": img_url,
        "description": pokemon.description,
    }

    if pokemon.previous_evolution:
        pokemon_page["previous_evolution"] = {
            "title_ru": pokemon.previous_evolution.title_ru,
            "pokemon_id": pokemon.previous_evolution.id,
            "img_url": request.build_absolute_uri(pokemon.previous_evolution.image.url)
            if pokemon.previous_evolution.image
            else "",
        }

    next_evolution = Pokemon.objects.filter(previous_evolution=pokemon).first()

    if next_evolution:
        pokemon_page["next_evolution"] = {
            "title_ru": next_evolution.title_ru,
            "pokemon_id": next_evolution.id,
            "img_url": request.build_absolute_uri(next_evolution.image.url)
            if next_evolution.image
            else "",
        }

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemon_entities = PokemonEntity.objects.filter(pokemon=pokemon)
    for entity in pokemon_entities:
        add_pokemon(folium_map, entity.lat, entity.lon, img_url)

    return render(
        request,
        "pokemon.html",
        context={
            "map": folium_map._repr_html_(),
            "pokemon": pokemon_page,
        },
    )
