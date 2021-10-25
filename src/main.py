import logging

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

from .bot_handlers import send_result_spell_check, start

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


def start_bot(token: str, port: int) -> None:
    """Start the bot."""
    updater = Updater(token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(
        MessageHandler(
            Filters.text & ~Filters.command, send_result_spell_check
        )
    )
    updater.start_webhook(
        listen="0.0.0.0",
        port=port,
        url_path=token,
        webhook_url="https://echobot-webhook.herokuapp.com/" + token,
    )
    updater.idle()
