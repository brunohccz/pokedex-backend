from src.app.fastapi.presenters.find_pokemon_presenter import FindPokemonPresenter
from src.domain.entities.pokemon import Pokemon
from src.interactor.dtos.find_pokemon_dtos import FindPokemonOutputDto


def test_find_pokemon_presenter(fixture_pokemon):
    pokemon = Pokemon(**fixture_pokemon)
    output_dto = FindPokemonOutputDto(pokemon)
    presenter = FindPokemonPresenter()
    assert presenter.present(output_dto) == {'abilities': [],
                                             'category': '',
                                             'height': '2\' 04"',
                                             'id': 1,
                                             'name': 'Bulbasaur',
                                             'species': {},
                                             'sprites': None,
                                             'stats': None,
                                             'types': None,
                                             'weaknesses': [],
                                             'weight': 17.6}
