from .list_pokemons_dtos import ListPokemonsInputDto


def test_list_pokemons_input_dto_valid(fixture_pokemon):
    input_dto = ListPokemonsInputDto(
        limit=None,
        offset=None,
    )
    assert input_dto.limit is None
    assert input_dto.offset is None
    assert input_dto.to_dict() == {"limit": None, "offset": None}