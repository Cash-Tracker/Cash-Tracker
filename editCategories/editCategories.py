from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext import ConversationHandler, CommandHandler, MessageHandler
from telegram.ext.filters import Filters



category = 0


def editCategories(update: Update, context: CallbackContext):
    update.message.reply_text("Please enter all the new categories: ")
    return category


def askCategory(update: Update, context: CallbackContext):
    categories = update.message.text
    categories = categories.split(',')
    categories = list(map(str.strip, categories))
    context.user_data['categories'] = categories

    categoriesString = "\n".join(categories)
    update.message.reply_text(f'''Awesome!
Here are the categories you entered:
{categoriesString}

They have been updated.
''')
    return ConversationHandler.END


def cancel(update: Update, context: CallbackContext):
    pass







conv_handler_editCategories = ConversationHandler(
    entry_points=[CommandHandler("editcategories", editCategories)],
    states={
        category: [MessageHandler(~Filters.command, askCategory)],
    },
    fallbacks=[CommandHandler("cancel", cancel)],
)