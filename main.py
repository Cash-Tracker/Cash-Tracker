from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import mysql.connector as DatabaseConnector
from dotenv import load_dotenv
import os


# ENVS
load_dotenv()
telegramKey = os.getenv("telegramKey")
databaseLocalhostPassword = os.getenv("databaseLocalhostPassword")


# ALL FUNCTIONS
import spending.spend
import summary.summary




# TELEGRAM API
try:
    updater = Updater(telegramKey,
                    use_context=True)
except:
    print("Error in connecting to telegram API")



# MYSQL DATABASE CONNECTION
try:
    db = DatabaseConnector.connect(
    host = 'localhost',
    user = 'BetterMoney', 
    passwd = databaseLocalhostPassword, 
    database = 'BetterMoney')
    print("Successfully Connected to MySQL Database")
except:
    print("Something is Wrong with MySQL Connection!")




def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Hello There! We are BetterMoney. We will help you manage your expenses and track them. We are currently under development and will be live soon!")



updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('spent', spending.spend.spent))
updater.dispatcher.add_handler(CommandHandler('summary', summary.summary.summary))




updater.start_polling()
