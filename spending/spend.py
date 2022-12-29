from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext


def spent(update: Update, context: CallbackContext):
    update.message.reply_text("placeholderText for Spent")

    



