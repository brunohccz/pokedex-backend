from fastapi import APIRouter

from src.app.fastapi.controllers.FindPokemonController import FindPokemonController
from src.domain.entities.pokemon import Pokemon

router = APIRouter()


@router.get("/pokemons/{pokemon_id}", summary="Find a pokemon by id")
async def find_pokemon(pokemon_id: int):
    controller = FindPokemonController()
    controller.get_pokemon_id({"id": pokemon_id})
    return await controller.execute()
