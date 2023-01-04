from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext



# Shreya

def summary(update: Update, context: CallbackContext):
    update.message.reply_text("placeholderText For Summary")
    # responseList = [[amountSpent1: int, Category1: str, DateTime1: str], [amountSpent2, Category2, DateTime2: str]]
    # responseList = getData(str:YYYY-MM)
    # Request which will be a string => YYYY-MM
    # Suggestion: library called PrettyTable


    # DUMMY REQUEST
    #responseList = database.getSummary("2022", "12", <ID>)
    responseList = [[50, 'food', '2022-12-15 20:00:00'], [1000, 'clothes', '2022-12-15 15:00:00']]

    # You need to write some code here to depict this data

responseList = [[50, 'food', '2022-12-15 20:00:00'], [1000, 'clothes', '2022-12-15 15:00:00']]

totalmon= {}

for i in responseList:
    val= i[0]
    categ=i[1]
    if categ in totalmon:
        totalmon[categ] += val
    else: 
        totalmon[categ] = val

print(totalmon)

import matplotlib.pyplot as plt


lab = []
vals = []
for categ, total in totalmon.items(): #to clear my confusion categ is the key, total is the value
    lab.append(categ)
    vals.append(total)

fig1, ax1 = plt.subplots()
ax1.pie(vals, labels=lab)
ax1.axis('equal')  

plt.show()
