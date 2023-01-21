# Synoptic TG Bot

This is bot which receives a geolocation from the user and returns weather data in this location

-- --

## Bot structure

- [synoptic_tg_bot.py](https://github.com/fomaaq/synoptic_tg_bot/blob/main/synoptic_tg_bot.py) -- the main executable file of the bot
- [testing.py](https://github.com/fomaaq/synoptic_tg_bot/blob/main/testing.py) -- contains methods for unit tests
- [error/errors_handler.py](https://github.com/fomaaq/synoptic_tg_bot/blob/main/error/errors_handler.py) -- contains methods for error handling, sending logs, and sending error messages to the user
- [service/weather_service.py](https://github.com/fomaaq/synoptic_tg_bot/blob/main/service/weather_service.py) -- contains methods for generating and sending a request to the server
- [utils](https://github.com/fomaaq/synoptic_tg_bot/tree/main/utils) -- contains a set of utils for the bot:
- - [utils/answer_utils.py](https://github.com/fomaaq/synoptic_tg_bot/blob/main/utils/answer_utils.py) -- contains methods for creating and sending responses to the user
- - [utils/data_utils.py](https://github.com/fomaaq/synoptic_tg_bot/blob/main/utils/data_utils.py) -- contains methods for processing data received from the weather service
- - [utils/testing_utils.py](https://github.com/fomaaq/synoptic_tg_bot/blob/main/utils/testing_utils.py) -- contains methods for testing utils

-- --

## Bot creation motivation

I created this bot for:
- create my own project on python
- create a telegram bot
- try third-party python libraries
- write and use unit tests

-- --

## Preview

Screenshots of the bot's reaction to various actions:
- Initial open
- Command **/start**
- Bot answer
- Answer to the other content


|![Preview](https://raw.githubusercontent.com/fomaaq/synoptic_tg_bot/main/imgs/preview.png) |![Start](https://raw.githubusercontent.com/fomaaq/synoptic_tg_bot/main/imgs/start.png) |
|--|--|
![Location](https://raw.githubusercontent.com/fomaaq/synoptic_tg_bot/main/imgs/location.png) |![Text](https://raw.githubusercontent.com/fomaaq/synoptic_tg_bot/main/imgs/text.png)

Detailed descriptions of modules and methods are given in the documentation

-- --

## Start action
When the bot is launched, unit tests are run first, after which the bot itself is launched. In the terminal it is displayed like this:
![Bot_start](https://raw.githubusercontent.com/fomaaq/synoptic_tg_bot/main/imgs/bot_start.jpg)

-- --

## How to run
Python version 3.10 was used at launch

The requirements are specified in the [requirements.txt](https://github.com/fomaaq/synoptic_tg_bot/blob/main/requirements.txt)
