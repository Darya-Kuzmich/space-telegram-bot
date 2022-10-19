from typing import Any

import redis

from decorators import backoff
from config import settings


class RedisStorage:

    def __init__(self, host: str, port: int, db: int) -> None:

        self.client = redis.Redis(
            host=host,
            port=port,
            db=db,
            decode_responses=True
        )

    @backoff(**settings.backoff_settings.dict())
    def save_state(self, key: str, value: Any) -> None:
        settings.logger.info('Save state to Redis')
        self.client.set(key, value)

    @backoff(**settings.backoff_settings.dict())
    def get_state(self, key: str) -> Any:
        settings.logger.info('Get state from Redis')
        return self.client.get(key)

    @backoff(**settings.backoff_settings.dict())
    def exist_state(self, key: str) -> bool:
        return self.client.exists(key)
