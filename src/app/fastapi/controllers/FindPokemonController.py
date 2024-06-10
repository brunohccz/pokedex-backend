from src.app.fastapi.interfaces.fastapi_controller_interface import FastAPIControllerInterface
from src.app.fastapi.presenters.find_pokemon_presenter import FindPokemonPresenter
from src.infra.cache.redis_cache import RedisCache
from src.infra.clients.httpx_client import HttpxClient
from src.infra.repositories.pokemon_pokeapi_repository import PokemonPokeAPIRepository
from src.interactor.dtos.find_pokemon_dtos import FindPokemonInputDto
from src.interactor.use_cases.find_pokemon import FindPokemonUseCase


class FindPokemonController(FastAPIControllerInterface):
    def __init__(self):
        self.input_dto: FindPokemonInputDto

    def get_pokemon_id(self, params: dict) -> None:
        self.input_dto = FindPokemonInputDto(
            id=params.get("id")
        )

    async def execute(self) -> dict:
        http_client = HttpxClient()
        cache_client = RedisCache()
        repository = PokemonPokeAPIRepository(http_client, cache_client)
        presenter = FindPokemonPresenter()
        use_case = FindPokemonUseCase(presenter, repository)
        return await use_case.execute(self.input_dto)
