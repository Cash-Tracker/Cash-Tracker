from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters


# ALL FUNCTIONS
import spending.spend
import summary.summary



try:
    updater = Updater("5723259015:AAEgN-R-Vl4i9UYz5XLLQT1qUs-AQSsocrA",
                    use_context=True)
except:
    print("Error in connecting to telegram API")



def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Hello There! We are BetterMoney. We will help you manage your expenses and track them. We are currently under development and will be live soon!")



updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('spent', spending.spend.spent))
updater.dispatcher.add_handler(CommandHandler('summary', summary.summary.summary))




updater.start_polling()
