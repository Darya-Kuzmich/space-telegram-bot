import time
import datetime
from urllib.parse import urljoin

import telegram
import requests
import schedule
from bs4 import BeautifulSoup
from pydantic import ValidationError
from dateutil import parser

from config import settings, NewsCard
from storages import RedisStorage

redis_storage = RedisStorage(**settings.redis.dict())


def get_html() -> requests.Response.text:
    try:
        response = requests.get(url=settings.ASTRO_NEWS_URL, verify=False)
        response.raise_for_status()
        response.encoding = 'utf-8'
        return response.text
    except (requests.exceptions.HTTPError,
            requests.exceptions.RequestException,
            requests.exceptions.ConnectionError,
            requests.exceptions.Timeout) as error:
        raise error


def get_news_cards(html: requests.Response.text) -> list[NewsCard]:
    soup = BeautifulSoup(html, features='lxml')
    a_tags = soup.find_all('a', class_='name')

    news_cards = []

    if redis_storage.exist_state('latest_news_date'):
        state = parser.parse(
            redis_storage.get_state('latest_news_date')
        )
    else:
        state = parser.parse('2000-01-01')

    for news in a_tags:
        news_title = news.text

        news_relative_link = news.get('href')
        news_link = urljoin(settings.PLANETARIUM_URL, news_relative_link)

        news_date = news.find_next_sibling('div').text
        news_date = parser.parse(news_date, dayfirst=True)

        if news_date.date() >= state.date():
            try:
                news = NewsCard(
                    title=news_title,
                    link=news_link,
                    date=news_date,
                )
                news_cards.append(news)
            except ValidationError as error:
                raise error
    redis_storage.save_state('latest_news_date', str(datetime.date.today()))
    return news_cards


def main():
    settings.logger.info('Into the space!')
    bot_client = telegram.Bot(token=settings.TELEGRAM_TOKEN)

    try:
        html = get_html()
        news_cards = get_news_cards(html=html)

        if not news_cards:
            bot_client.send_message(
                chat_id=settings.TELEGRAM_CHAT_ID,
                text='\U00002b1b No news today',
            )
        else:
            bot_client.send_message(
                chat_id=settings.TELEGRAM_CHAT_ID,
                text='\U00002b50 Latest news',
            )

            for news in news_cards:
                message = f'{news.title}\n {news.link}\n {news.date}\n'
                bot_client.send_message(
                    chat_id=settings.TELEGRAM_CHAT_ID,
                    text=message,
                )

    except Exception as error:
        settings.logger.exception('Error')
        bot_client.send_message(
            chat_id=settings.TELEGRAM_CHAT_ID,
            text=f'\U0000203C Ooops! Something wrong: {error}',
        )


if __name__ == '__main__':

    schedule.every().day.at('9:30').do(main)

    while True:
        schedule.run_pending()
        time.sleep(1)
