from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext import ConversationHandler, CommandHandler, MessageHandler
from telegram.ext.filters import Filters
from telegram import KeyboardButton, ReplyKeyboardMarkup
from spending.getCurrentTime import getCurrentTime
from database.database import pushSpent

Amount, Category, onWhat, Note = range(4)



def spent(update: Update, context: CallbackContext):
    update.message.reply_text("How much did you spend?")
    return Amount



def amount_conv(update: Update, context: CallbackContext):
    context.user_data["Amount"] = update.message.text
    amount = context.user_data["Amount"]
    update.message.reply_text(f"Okay, On what did you spend {amount} on?")
    return onWhat



def onWhat_conv(update: Update, context: CallbackContext):
    context.user_data["onWhat"] = update.message.text
    choices = context.user_data["categories"]
    reply_markup = ReplyKeyboardMarkup([[KeyboardButton(choice)] for choice in choices], one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text("Cool! What category does it belong to?", reply_markup=reply_markup)
    return Category


def category_conv(update: Update, context: CallbackContext):
    context.user_data["Category"] = update.message.text
    update.message.reply_text("Awesome, Finally, Tell me a small note you want to add to this.")
    return Note



def note_conv(update: Update, context: CallbackContext):
    context.user_data["Note"] = update.message.text
    time = getCurrentTime()
    id = update.message.from_user["id"]
    amount = context.user_data["Amount"]
    category = context.user_data["Category"]
    onWhat = context.user_data["onWhat"]
    Note = context.user_data["Note"]

    # ID, amount, category, onWhat, note, datetime
    pushSpent(id, amount, category, onWhat, Note, time)
    update.message.reply_text("Done!")
    return ConversationHandler.END


def cancel(update: Update, context: CallbackContext):
    update.message.reply_text("Okay! Cancelled")
    return ConversationHandler.END




conv_handler_spent = ConversationHandler(
    entry_points=[CommandHandler("spent", spent)],
    states={
        Amount: [MessageHandler(Filters.text & Filters.regex('^[0-9]+$'), amount_conv)],
        onWhat: [MessageHandler(~Filters.command, onWhat_conv)],
        Category: [MessageHandler(~Filters.command, category_conv)],
        Note: [MessageHandler(~Filters.command, note_conv)],
    },
    fallbacks=[CommandHandler("cancel", cancel)],
)



    







    



