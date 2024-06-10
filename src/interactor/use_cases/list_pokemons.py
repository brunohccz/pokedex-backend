import asyncio

from src.interactor.dtos.list_pokemons_dtos import ListPokemonsOutputDto, ListPokemonsInputDto
from src.interactor.interfaces.presenters.list_pokemons_presenter import ListPokemonsPresenterInterface
from src.interactor.interfaces.presenters.list_xml_pokemons_presenter import ListXMLPokemonsPresenterInterface
from src.interactor.interfaces.repositories.pokemon_repository import PokemonRepositoryInterface


class ListPokemonsUseCase:
    def __init__(
            self,
            presenter: ListPokemonsPresenterInterface | ListXMLPokemonsPresenterInterface,
            repository: PokemonRepositoryInterface
    ):
        self.presenter = presenter
        self.repository = repository

    async def execute(self, input_dto: ListPokemonsInputDto):
        pokemons = await self.repository.list(
            limit=input_dto.limit,
            offset=input_dto.offset
        )
        # pokemons = asyncio.run(pokemons)
        output_dto = ListPokemonsOutputDto(pokemons)
        return self.presenter.present(output_dto)
