import xml.etree.ElementTree as ET
from src.app.fastapi.presenters.list_xml_pokemons_presenter import ListXMLPokemonsPresenter
from src.domain.entities.pokemon import Pokemon
from src.interactor.dtos.list_pokemons_dtos import ListPokemonsOutputDto


def test_list_xml_pokemons_presenter(fixture_pokemon):
    pokemon = Pokemon(**fixture_pokemon)
    output_dto = ListPokemonsOutputDto([pokemon])
    presenter = ListXMLPokemonsPresenter()
    result_xml = presenter.present(output_dto)

    expected_xml = (
        f"<?xml version='1.0' encoding='utf8'?>"
        f"<pokemons>"
        f"<pokemon>"
        f"<id>{pokemon.id}</id>"
        f"<name>{pokemon.name}</name>"
        f"</pokemon>"
        f"</pokemons>"
    )

    result_tree = ET.ElementTree(ET.fromstring(result_xml))
    expected_tree = ET.ElementTree(ET.fromstring(expected_xml))

    result_str = ET.tostring(result_tree.getroot(), encoding='utf8').decode('utf8')
    expected_str = ET.tostring(expected_tree.getroot(), encoding='utf8').decode('utf8')

    assert result_str == expected_str
