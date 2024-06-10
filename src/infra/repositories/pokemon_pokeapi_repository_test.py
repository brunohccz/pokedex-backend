from typing import Any

import pytest

from src.infra.repositories.pokemon_pokeapi_repository import PokemonPokeAPIRepository
from src.interactor.interfaces.cache_client import CacheClientInterface
from src.interactor.interfaces.http_client import HttpClientInterface
from src.domain.entities.pokemon import Pokemon


class MockHttpClient(HttpClientInterface):
    async def get(self, url: str, params: dict[str, Any] = None):
        return {
            "results": [
                {"name": "bulbasaur", "url": "https://pokeapi.co/api/v2/pokemon/1"},
                {"name": "ivysaur", "url": "https://pokeapi.co/api/v2/pokemon/2"}
            ]
        }


class MockCacheClient(CacheClientInterface):
    async def get_value(self, key):
        pass

    async def set_value(self, key: str, value: str, expire: int = None):
        pass


@pytest.mark.asyncio
async def test_list():
    http_client = MockHttpClient()
    cache_client = MockCacheClient()
    repository = PokemonPokeAPIRepository(http_client, cache_client)
    pokemons = await repository.list(limit=2, offset=0)
    assert len(pokemons) == 2
    assert isinstance(pokemons[0], Pokemon)
    assert isinstance(pokemons[1], Pokemon)


@pytest.mark.asyncio
async def test_find_by_id():
    http_client = MockHttpClient()
    cache_client = MockCacheClient()
    repository = PokemonPokeAPIRepository(http_client, cache_client)
    pokemon = await repository.find_by_id(1)
    assert isinstance(pokemon, Pokemon)
