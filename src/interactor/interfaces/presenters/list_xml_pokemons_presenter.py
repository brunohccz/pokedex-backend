from abc import ABC, abstractmethod

from src.interactor.dtos.list_pokemons_dtos import ListPokemonsOutputDto


class ListXMLPokemonsPresenterInterface(ABC):
    @abstractmethod
    def present(self, output_dto: ListPokemonsOutputDto) -> str:
        pass
