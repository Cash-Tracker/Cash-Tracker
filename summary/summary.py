from telegram import Update
from telegram.ext import CallbackContext
import matplotlib
matplotlib.use("Agg")
from database.database import getSummary
from datetime import datetime, timedelta

from summary.getTempImg import getTempImg


async def summary(update: Update, context: CallbackContext):
    # await update.message.reply_text("placeholderText For Summary")
    # responseList = [[amountSpent1: int, Category1: str, DateTime1: str], [amountSpent2, Category2, DateTime2: str]]
    # responseList = getData(str:YYYY-MM)
    # Request which will be a string => YYYY-MM
    # Suggestion: library called PrettyTable


    curr_date = datetime.now().strftime("%Y-%m")
    curr_date = datetime.strptime(curr_date, "%Y-%m")
    

    # Subtract one month from the current date
    # prev_date = curr_date - timedelta(days=30)
    # DEMONSTRATION PURPOSES:
    prev_date = curr_date


    userID = update.message.from_user["id"]
    responseList = getSummary(prev_date.year, prev_date.month, userID)
    if responseList == []:
        await update.message.reply_text("You have no data from the previous month. Try the /summaryFromGivenMonth command.")
    # time = getCurrentTime()
    # You need to write some code here to depict this data
    else:
        totalmon = {}

        for i in responseList:
            val= i[0]
            categ=i[1]
            if categ in totalmon:
                totalmon[categ] += val
            else: 
                totalmon[categ] = val





        lables = []
        vals = []
        for categ, total in totalmon.items(): #to clear my confusion categ is the key, total is the value
            lables.append(categ)
            vals.append(total)

        temp = getTempImg(lables, vals)
        update.message.reply_photo(temp)
        temp.close()




    