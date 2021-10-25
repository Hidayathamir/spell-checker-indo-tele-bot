from os import environ
from src.main import start_bot


bot_token = environ.get("bot_token", "")
port = environ.get("PORT", 1234)
start_bot(bot_token, port)
