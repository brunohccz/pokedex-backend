![tests](https://github.com/brunohccz/pokedex-backend/workflows/pytesting/badge.svg) &nbsp; ![code coverage](https://raw.githubusercontent.com/brunohccz/pokedex-backend/coverage-badge/coverage.svg?raw=true)

# Pokedex API

Este projeto é uma API que permite aos usuários buscar informações sobre Pokemons.

## Requisitos

- Python 3.11
- Docker
- Poetry

## Configuração

1. Clone o repositório para o seu ambiente local:

```bash
git clone https://github.com/brunohccz/pokedex-backend.git
cd pokedex-backend
```

2. Instale as dependências do projeto:

```bash
pip install poetry
poetry install
```

## Execução com Docker Compose

Para executar a aplicação usando Docker Compose, você precisa ter o Docker instalado em seu sistema.

Primeiro, construa e inicie os serviços definidos no arquivo `docker-compose.yml`:

```bash
docker compose up -d
```

A aplicação estará disponível em `http://localhost:8000`.

Para parar e remover os containers, redes e volumes definidos no arquivo `docker-compose.yml`, use o seguinte comando:

```bash
docker compose down
```

## Testes

Para executar os testes, use o seguinte comando:

```bash
make test
```

## Documentação da API

A documentação da API está disponível em `http://localhost:8000/docs` quando a aplicação está em execução.
