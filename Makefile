install:
	poetry install

init:
	poetry run uvicorn src.app.fastapi.main:app --reload --host 0.0.0.0 --port 8002

test: clean-test
	poetry run pytest

build: clean-cache
	DOCKER_BUILDKIT=1 docker build --platform linux/amd64 --ssh default --tag pokedex-api .

clean-test:
	rm -rf .pytest-cache

clean-cache:
	find . | grep /__pycache__ | xargs rm -rf
	find . | grep *.pyc | xargs rm -rf
	find . | grep *.pyo | xargs rm -rf
