from telegram.ext import Application
from telegram import Update
from telegram.ext import ConversationHandler
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
import telegram.ext.filters as filters


from dotenv import load_dotenv
import os


# ENVS
load_dotenv()
telegramKey = os.getenv("telegramKey")


# ALL FUNCTIONS
from spending.spend import conv_handler_spent
from summary.summary import summary
from editCategories.editCategories import conv_handler_editCategories




# TELEGRAM API
try:
    application = Application.builder().token(telegramKey).build()
    print("Successfully Connected to Telegram API")
except Exception as e:
    print(f"Error in connecting to telegram API {e}")




async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(f"Hello There! We are BetterMoney. We will help you manage your expenses and track them. Tell me a bunch of categories you usually spend your money on. separate the categories with a comma: ")
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

You can modify these using the /editCategories command later. You can now start to use the bot :)''')

    return ConversationHandler.END





category = 0
conv_handler_start = ConversationHandler(
    entry_points=[CommandHandler("start", start)],
    states={
        category: [MessageHandler(~filters.COMMAND, askCategory)],
    },
    fallbacks=[],
)



application.add_handler(conv_handler_spent)
application.add_handler(CommandHandler('summary', summary))
application.add_handler(conv_handler_start)
application.add_handler(conv_handler_editCategories)




application.run_polling()
