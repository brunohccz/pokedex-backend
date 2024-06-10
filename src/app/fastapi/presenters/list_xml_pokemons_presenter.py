from xml.etree.ElementTree import Element, tostring
from src.interactor.dtos.list_pokemons_dtos import ListPokemonsOutputDto
from src.interactor.interfaces.presenters.list_xml_pokemons_presenter import ListXMLPokemonsPresenterInterface


class ListXMLPokemonsPresenter(ListXMLPokemonsPresenterInterface):
    def present(self, output_dto: ListPokemonsOutputDto) -> str:
        sorted_pokemons = sorted(output_dto.pokemons, key=lambda pokemon: pokemon.name)
        root = Element('pokemons')
        for pokemon in sorted_pokemons:
            pokemon_element = Element('pokemon')
            id_element = Element('id')
            id_element.text = str(pokemon.id)
            name_element = Element('name')
            name_element.text = pokemon.name

            pokemon_element.append(id_element)
            pokemon_element.append(name_element)
            root.append(pokemon_element)

        return tostring(root, encoding='utf8', method='xml')
