from src.app.fastapi.interfaces.fastapi_controller_interface import FastAPIControllerInterface
from src.app.fastapi.presenters.list_xml_pokemons_presenter import ListXMLPokemonsPresenter
from src.infra.cache.redis_cache import RedisCache
from src.infra.clients.httpx_client import HttpxClient
from src.infra.repositories.pokemon_pokeapi_repository import PokemonPokeAPIRepository
from src.interactor.dtos.list_pokemons_dtos import ListPokemonsInputDto
from src.interactor.use_cases.list_pokemons import ListPokemonsUseCase


class ListXMLPokemonController(FastAPIControllerInterface):
    def __init__(self):
        self.input_dto: ListPokemonsInputDto

    def get_search_params(self, params: dict) -> None:
        self.input_dto = ListPokemonsInputDto(
            limit=params.get("limit"),
            offset=params.get("offset")
        )

    async def execute(self) -> str:
        http_client = HttpxClient()
        cache_client = RedisCache()
        repository = PokemonPokeAPIRepository(http_client, cache_client)
        presenter = ListXMLPokemonsPresenter()
        use_case = ListPokemonsUseCase(presenter, repository)
        return await use_case.execute(self.input_dto)
