from redis import asyncio

import configs.config
from src.interactor.interfaces.cache_client import CacheClientInterface


class RedisCache(CacheClientInterface):
    def __init__(self):
        self.redis_url = configs.config.REDIS_URL
        self.redis = None

    async def connect(self):
        if self.redis is None:
            self.redis = await asyncio.from_url(self.redis_url, encoding="utf-8", decode_responses=True)

    async def set_value(self, key, value, expire=None):
        await self.connect()
        await self.redis.set(key, value, ex=expire)

    async def get_value(self, key):
        await self.connect()
        return await self.redis.get(key)

    async def close(self):
        if self.redis:
            await self.redis.close()
