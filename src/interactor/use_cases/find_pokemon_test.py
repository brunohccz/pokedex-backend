import pytest

from src.domain.entities.pokemon import Pokemon
from src.interactor.interfaces.presenters.find_pokemon_presenter import FindPokemonPresenterInterface
from src.interactor.interfaces.repositories.pokemon_repository import PokemonRepositoryInterface
from src.interactor.use_cases import find_pokemon


@pytest.mark.asyncio
async def test_find_pokemon(mocker, fixture_pokemon):
    pokemon = Pokemon(**fixture_pokemon)
    presenter_mock = mocker.patch.object(
        FindPokemonPresenterInterface,
        'present',
    )
    repository_mock = mocker.patch.object(
        PokemonRepositoryInterface,
        'find_by_id',
    )
    repository_mock.find_by_id.return_value = pokemon
    presenter_mock.present.return_value = "Test output"
    use_case = find_pokemon.FindPokemonUseCase(
        presenter=presenter_mock,
        repository=repository_mock,
    )
    input_dto = find_pokemon.FindPokemonInputDto(id=1)
    result = await use_case.execute(input_dto)
    repository_mock.find_by_id.assert_called_once_with(1)
    output_dto = find_pokemon.FindPokemonOutputDto(pokemon)
    presenter_mock.present.assert_called_once_with(output_dto)
    assert result == "Test output"
