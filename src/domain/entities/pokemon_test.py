from .pokemon import Pokemon


def test_pokemon_from_dict(fixture_pokemon):
    pokemon = Pokemon.from_dict(fixture_pokemon)
    assert pokemon.id == fixture_pokemon['id']
    assert pokemon.name == fixture_pokemon['name']
    assert pokemon.height == fixture_pokemon['height']
    assert pokemon.weight == fixture_pokemon['weight']


def test_pokemon_to_dict(fixture_pokemon):
    pokemon = Pokemon.from_dict(fixture_pokemon)
    assert pokemon.to_dict() == fixture_pokemon


def test_pokemon_equality(fixture_pokemon):
    pokemon1 = Pokemon.from_dict(fixture_pokemon)
    pokemon2 = Pokemon.from_dict(fixture_pokemon)
    assert pokemon1 == pokemon2
