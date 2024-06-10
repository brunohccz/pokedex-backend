from src.interactor.dtos.find_pokemon_dtos import FindPokemonInputDto, FindPokemonOutputDto
from src.interactor.interfaces.presenters.find_pokemon_presenter import FindPokemonPresenterInterface
from src.interactor.interfaces.repositories.pokemon_repository import PokemonRepositoryInterface


class FindPokemonUseCase:
    def __init__(
            self,
            presenter: FindPokemonPresenterInterface,
            repository: PokemonRepositoryInterface
    ):
        self.presenter = presenter
        self.repository = repository

    async def execute(self, input_dto: FindPokemonInputDto) -> dict:
        pokemon = await self.repository.find_by_id(input_dto.id)
        output_dto = FindPokemonOutputDto(pokemon)
        return self.presenter.present(output_dto)