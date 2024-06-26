from dataclasses import dataclass, asdict

from src.domain.entities.pokemon import Pokemon


@dataclass
class FindPokemonInputDto:
    id: int

    def to_dict(self):
        return asdict(self)


@dataclass
class FindPokemonOutputDto:
    pokemon: Pokemon
