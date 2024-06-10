from fastapi import APIRouter, Response
from src.app.fastapi.controllers.ListPokemonController import ListPokemonController
from src.app.fastapi.controllers.ListXMLPokemonController import ListXMLPokemonController

router = APIRouter()


@router.get("/pokemons", summary="List pokemons", response_description="List of pokemons")
async def list_pokemons(limit: int = None, offset: int = None):
    controller = ListPokemonController()
    controller.get_search_params({"limit": limit, "offset": offset})
    return await controller.execute()


@router.get("/pokemons/xml", summary="List pokemons in XML", response_description="List of pokemons in XML")
async def list_xml_pokemons(limit: int = None, offset: int = None):
    controller = ListXMLPokemonController()
    controller.get_search_params({"limit": limit, "offset": offset})
    xml_str = await controller.execute()
    headers = {
        "Content-Disposition": "attachment; filename=pokemons.xml",
        "Content-Type": "application/xml"
    }
    return Response(content=xml_str, media_type="application/xml", headers=headers)
