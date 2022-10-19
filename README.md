![workflow](https://github.com/Darya-Kuzmich/space-telegram-bot/actions/workflows/space-bot-workflow.yml/badge.svg)
# Space Telegram Bot

## Description
***

The bot parses the [Moscow planetarium](https://www.planetarium-moscow.ru/) 
website every day and sends news. If there is no fresh news, then the bot sends a message `No news today`.
If something happens, the bot will also send an error message.

## Requirements
***
**Space telegram bot** requires [Docker](https://www.docker.com/) and [make](https://www.gnu.org/software/make/) to run.
You also need a telegram bot.

## Tech
***
**Space telegram bot** uses:
* [Python 3.10](https://www.python.org/)
* [Python-Telegram-Bot](https://pypi.org/project/python-telegram-bot/)
* [Beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Requests](https://requests.readthedocs.io/en/latest/)
* [Schedule](https://github.com/dbader/schedule)
* [Redis-Py](https://redis-py.readthedocs.io/en/stable/)
* [Pydantic](https://pypi.org/project/pydantic/)
* [Python-Dotenv](https://pypi.org/project/python-dotenv/)


## Quick start
***
1. Clone this repo.
> git clone [git@github.com:Darya-Kuzmich/space-telegram-bot.git](https://github.com/Darya-Kuzmich/space-telegram-bot)
2. Place an `.env` file in the root of the project. An example can be found in the [env.example](env.example) file.
Specify your `TELEGRAM_TOKEN` and `TELEGRAM_CHAT_ID` variables.
3. Change in the [bot.py](bot.py) the desired time for receiving the news if you want. 
   (for more information about the schedule see [schedule library](https://github.com/dbader/schedule))
4. Then from the root directory of the project run the next command in the terminal.
> make build-up

After executing this command, two containers should be built and launched:
* space_bot
* redis_space_bot
5. At the time specified in the schedule, astro news will come to your telegram bot. Enjoy! 😊

## Features
***
To see all available commands, run 
> make help

If you want, you can add other commands to the [Makefile](Makefile).


## License
***
MIT

## Author
***
Darya Let'sRock Kuzmich