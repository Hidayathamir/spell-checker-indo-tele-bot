from decouple import config

from src.main import start_bot

start_bot(config("bot_token"))
