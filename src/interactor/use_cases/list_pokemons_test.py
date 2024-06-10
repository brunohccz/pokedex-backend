import pytest

from src.interactor.dtos.list_pokemons_dtos import ListPokemonsOutputDto, ListPokemonsInputDto
from src.interactor.use_cases import list_pokemons
from src.interactor.interfaces.presenters.list_pokemons_presenter import ListPokemonsPresenterInterface
from src.interactor.interfaces.repositories.pokemon_repository import PokemonRepositoryInterface
from src.domain.entities.pokemon import Pokemon


@pytest.mark.asyncio
async def test_list_pokemons(mocker, fixture_pokemon):
    pokemon = Pokemon(**fixture_pokemon)
    presenter_mock = mocker.patch.object(
        ListPokemonsPresenterInterface,
        'present',
    )
    repository_mock = mocker.patch.object(
        PokemonRepositoryInterface,
        'list',
    )
    repository_mock.list.return_value = [pokemon]
    presenter_mock.present.return_value = "Test output"
    use_case = list_pokemons.ListPokemonsUseCase(
        presenter=presenter_mock,
        repository=repository_mock,
    )
    input_dto = ListPokemonsInputDto()
    result = await use_case.execute(input_dto)
    repository_mock.list.assert_called_once()
    output_dto = ListPokemonsOutputDto([pokemon])
    presenter_mock.present.assert_called_once_with(output_dto)
    assert result == "Test output"
