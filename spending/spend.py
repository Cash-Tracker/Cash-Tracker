from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import ConversationHandler, CommandHandler, MessageHandler
import telegram.ext.filters as filters
from telegram import KeyboardButton, ReplyKeyboardMarkup
from spending.getCurrentTime import getCurrentTime
from database.database import pushSpent

Amount, Category, onWhat, Note = range(4)



async def spent(update: Update, context: CallbackContext):
    await update.message.reply_text("How much did you spend?")
    return Amount



async def amount_conv(update: Update, context: CallbackContext):
    context.user_data["Amount"] = update.message.text
    amount = context.user_data["Amount"]
    await update.message.reply_text(f"Okay, On what did you spend {amount} on?")
    return onWhat



async def onWhat_conv(update: Update, context: CallbackContext):
    context.user_data["onWhat"] = update.message.text
    choices = context.user_data["categories"]
    reply_markup = ReplyKeyboardMarkup([[KeyboardButton(choice)] for choice in choices], one_time_keyboard=True, resize_keyboard=True)
    await update.message.reply_text("Cool! What category does it belong to?", reply_markup=reply_markup)
    return Category


async def category_conv(update: Update, context: CallbackContext):
    context.user_data["Category"] = update.message.text
    await update.message.reply_text("Awesome, Finally, Tell me a small note you want to add to this.")
    return Note



async def note_conv(update: Update, context: CallbackContext):
    context.user_data["Note"] = update.message.text
    time = getCurrentTime()
    id = update.message.from_user["id"]
    amount = context.user_data["Amount"]
    category = context.user_data["Category"]
    onWhat = context.user_data["onWhat"]
    Note = context.user_data["Note"]

    # ID, amount, category, onWhat, note, datetime
    pushSpent(id, amount, category, onWhat, Note, time)
    await update.message.reply_text("Done!")
    return ConversationHandler.END


async def cancel(update: Update, context: CallbackContext):
    await update.message.reply_text("Okay! Cancelled")
    return ConversationHandler.END




conv_handler_spent = ConversationHandler(
    entry_points=[CommandHandler("spent", spent)],
    states={
        Amount: [MessageHandler(filters.TEXT & filters.Regex('^[0-9]+$'), amount_conv)],
        onWhat: [MessageHandler(~filters.COMMAND, onWhat_conv)],
        Category: [MessageHandler(~filters.COMMAND, category_conv)],
        Note: [MessageHandler(~filters.COMMAND, note_conv)],
    },
    fallbacks=[CommandHandler("cancel", cancel)],
)



    







    



