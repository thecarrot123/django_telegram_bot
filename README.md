# Link Django User To Telegram Bot

## About the project 

This project is about linking a django user with their telegram account where they can:
* Send data from server to a specific user telegram (e.g. notifications, confirmation code, etc.).
* Receive data from user via telegram bot and handle some requests (e.g. some info about the user).

## Requirements

* python3.8

## How To Run

* Install requirements:
```bash
pip install -r requirements.txt
```

* Add `django_telegram_bot` file to your django project directory then in your django project `settings.py` file add `django_telegram_bot` to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    '..',
    '..',
    'django_telegram_bot',
]
```

* Also in `settings.py` file add telegram bot information:

```python
TELEGRAM = {
    "token": "Your bot token goes here",
    "bot_name": "@Your_bot_name_goes_here"
}
```
> For more information about telegram bots visits this [link](https://www.freecodecamp.org/news/how-to-create-a-telegram-bot-using-python/)

* In terminal run the following commands:

    - Make migration files:
    ```bash
    python3 manage.py makemigrations django_telegram_bot
    ```
    - Migrate to database:
    ```bash
    python3 manage.py migrate django_telegram_bot
    ```
    - Start the bot with the following command:
    ```bash
    python3 manage.py runbot
    ```
    > This command will only run the bot and will not run the server.
    > To run the server you should run something like `python3 manage.py runserver 0.0.0.0:8080` in another terminal.

## Notes

* Alias should be unique for users.
* Sending `link_to_telegram` request to a linked user will save the new `alias` and will set `chat_id` to `None`.
* Check `api.yaml` to see existing endpoints.