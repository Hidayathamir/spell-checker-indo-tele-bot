from telegram import Update
from telegram.ext import CallbackContext

from .spell_check import get_wrong_word


def start(update: Update, _: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    if update.message is not None:
        update.message.reply_text(
            "Hallo. Silahkan chat text yang ingin di cek.",
            reply_to_message_id=update.message.message_id,
        )


def send_result_spell_check(update: Update, _: CallbackContext) -> None:
    """spell check in indonesian then send the wrong word"""
    if update.message is not None and update.message.text is not None:
        update.message.reply_text(
            "Tunggu sebentar ya.",
            reply_to_message_id=update.message.message_id,
        )
        user_text = update.message.text
        wrong_word = get_wrong_word(user_text)
        if wrong_word == "":
            update.message.reply_text(
                "Gak ada kata yang salah nih.",
                reply_to_message_id=update.message.message_id,
            )
        else:
            update.message.reply_text(
                f"Kata yang salah : {wrong_word}",
                reply_to_message_id=update.message.message_id,
            )
