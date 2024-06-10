from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.app.fastapi.routes.list_pokemons_router import router as list_pokemons
from src.app.fastapi.routes.find_pokemon_router import router as find_pokemon

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(list_pokemons, tags=["Pokemons"])
app.include_router(find_pokemon, tags=["Pokemons"])


@app.get("/")
async def root():
    return {"message": "Pokedex Api"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8003, timeout_keep_alive=60)
