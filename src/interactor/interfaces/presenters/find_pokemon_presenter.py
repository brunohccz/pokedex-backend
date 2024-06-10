from abc import ABC, abstractmethod
from src.interactor.dtos.find_pokemon_dtos import FindPokemonOutputDto


class FindPokemonPresenterInterface(ABC):
    @abstractmethod
    def present(self, output_dto: FindPokemonOutputDto) -> dict:
        pass
