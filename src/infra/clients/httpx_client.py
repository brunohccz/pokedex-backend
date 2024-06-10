from typing import Any
from httpx import AsyncClient

from src.interactor.interfaces.http_client import HttpClientInterface


class HttpxClient(HttpClientInterface):
    async def get(self, url: str, params: dict[str, Any] = None) -> dict[str, Any]:
        async with AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
