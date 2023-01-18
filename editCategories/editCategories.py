from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import ConversationHandler, CommandHandler, MessageHandler
import telegram.ext.filters as filters



category = 0


async def editCategories(update: Update, context: CallbackContext):
    await update.message.reply_text("Please enter all the new categories: ")
    return category


async def askCategory(update: Update, context: CallbackContext):
    categories = update.message.text
    categories = categories.split(',')
    categories = list(map(str.strip, categories))
    context.user_data['categories'] = categories

    categoriesString = "\n".join(categories)
    await update.message.reply_text(f'''Awesome!
Here are the categories you entered:
{categoriesString}

They have been updated.
''')
    return ConversationHandler.END


async def cancel(update: Update, context: CallbackContext):
    pass







conv_handler_editCategories = ConversationHandler(
    entry_points=[CommandHandler("editcategories", editCategories)],
    states={
        category: [MessageHandler(~filters.COMMAND, askCategory)],
    },
    fallbacks=[CommandHandler("cancel", cancel)],
)