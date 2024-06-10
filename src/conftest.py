import pytest


@pytest.fixture
def fixture_pokemon():
    return {
        'id': 1,
        'name': 'Bulbasaur',
        'height': 7,
        'weight': 80,
        'sprites': None,
        'stats': None,
        'types': None,
        'weaknesses': [],
        'abilities': [],
        'species': {}
    }
