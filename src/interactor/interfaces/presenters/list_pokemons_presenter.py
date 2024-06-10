from abc import ABC, abstractmethod
from src.interactor.dtos.list_pokemons_dtos import ListPokemonsOutputDto


class ListPokemonsPresenterInterface(ABC):
    @abstractmethod
    def present(self, output_dto: ListPokemonsOutputDto) -> dict:
        pass
