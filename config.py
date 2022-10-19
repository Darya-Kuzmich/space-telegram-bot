import logging.config
from datetime import date

from pydantic import BaseSettings, BaseModel, Field
from dotenv import load_dotenv

from logger import LOGGING

load_dotenv()

logging.config.dictConfig(LOGGING)
logger = logging.getLogger(__name__)


class NewsCard(BaseModel):
    title: str
    link: str
    date: date


class RedisCreds(BaseSettings):
    host: str = Field(..., env='REDIS_HOST')
    port: int = Field(..., env='REDIS_PORT')
    db: int = Field(..., env='REDIS_DB')


class BackoffParams(BaseModel):
    logger = logger
    start_sleep_time = 0.1
    factor = 2
    border_sleep_time = 10

    class Config:
        arbitrary_types_allowed = True


class Settings(BaseSettings):
    TELEGRAM_TOKEN: str = Field(..., env='MY_TELEGRAM_TOKEN')
    TELEGRAM_CHAT_ID: str = Field(..., env='MY_TELEGRAM_CHAT_ID')

    PLANETARIUM_URL: str = 'https://www.planetarium-moscow.ru'
    ASTRO_NEWS_URL: str = 'https://www.planetarium-moscow.ru/about/astro-news/'

    redis = RedisCreds()

    backoff_settings: BackoffParams = BackoffParams()

    logger = logger


settings = Settings()
