from src.interactor.dtos.list_pokemons_dtos import ListPokemonsOutputDto
from src.interactor.interfaces.presenters.list_pokemons_presenter import ListPokemonsPresenterInterface


class ListPokemonsPresenter(ListPokemonsPresenterInterface):
    def present(self, output_dto: ListPokemonsOutputDto) -> dict:
        sorted_pokemons = sorted(output_dto.pokemons, key=lambda pokemon: pokemon.name)
        return {
            'results': [
                {
                    'id': pokemon.id,
                    'name': pokemon.name,
                    'sprites': pokemon.sprites,
                    'types': pokemon.types,
                } for pokemon in sorted_pokemons
            ]
        }
