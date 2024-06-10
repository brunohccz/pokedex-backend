from src.app.fastapi.presenters.list_pokemons_presenter import ListPokemonsPresenter
from src.domain.entities.pokemon import Pokemon
from src.interactor.dtos.list_pokemons_dtos import ListPokemonsOutputDto


def test_list_pokemons_presenter(fixture_pokemon):
    pokemon = Pokemon(**fixture_pokemon)
    output_dto = ListPokemonsOutputDto([pokemon])
    presenter = ListPokemonsPresenter()
    assert presenter.present(output_dto) == {
        'results': [
            {
                'id': pokemon.id,
                'name': pokemon.name,
                'sprites': pokemon.sprites,
                'types': pokemon.types,
            }
        ]
    }