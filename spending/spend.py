from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext

import spending.getCurrentTime


# LAASYA
def spent(update: Update, context: CallbackContext):
    update.message.reply_text("placeholderText for Spent")


    # currentTime = getCurrentTime.getCurrentTime()








    



