from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.conversationhandler import ConversationHandler
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from dotenv import load_dotenv
import os



# ENVS
load_dotenv()
telegramKey = os.getenv("telegramKey")


# ALL FUNCTIONS
from spending.spend import conv_handler_spent
import summary.summary




# TELEGRAM API
try:
    updater = Updater(telegramKey,
                    use_context=True)
    print("Successfully Connected to Telegram API")
except:
    print("Error in connecting to telegram API")




def start(update: Update, context: CallbackContext):
    update.message.reply_text(f"Hello There! We are BetterMoney. We will help you manage your expenses and track them. Tell me a bunch of categories you usually spend your money on. separate the categories with a comma: ")
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

You can modify these using the /editCategories command later. You can now start to use the bot :)''')

    return ConversationHandler.END





category = 0
conv_handler_start = ConversationHandler(
    entry_points=[CommandHandler("start", start)],
    states={
        category: [MessageHandler(~Filters.command, askCategory)],
    },
    fallbacks=[],
)



updater.dispatcher.add_handler(conv_handler_spent)
updater.dispatcher.add_handler(CommandHandler('summary', summary.summary.summary))
updater.dispatcher.add_handler(conv_handler_start)





updater.start_polling()
