from src.interactor.dtos.find_pokemon_dtos import FindPokemonInputDto


def test_find_pokemons_dto_valid(fixture_pokemon):
    input_dto = FindPokemonInputDto(id=1)
    assert input_dto.id == 1
    assert input_dto.to_dict() == {"id": 1}