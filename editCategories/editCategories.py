from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import ConversationHandler, CommandHandler, MessageHandler
import telegram.ext.filters as filters

# Define states
CATEGORY, ADD_NEW_CATEGORIES, DELETE_CATEGORY = range(3)

# A dictionary to store user data
user_data = {}

# Function to start editing categories
async def editCategories(update: Update, context: CallbackContext):
    await update.message.reply_text("Please select an option:\n1. /addcategory to add new categories\n2. /deletecategory to delete a category")
    return CATEGORY

# Function to add new categories
async def addCategories(update: Update, context: CallbackContext):
    await update.message.reply_text("Please enter the new categories separated by commas: ")
    return ADD_NEW_CATEGORIES

# Function to handle adding new categories
async def handleAddCategories(update: Update, context: CallbackContext):
    categories = update.message.text
    categories = categories.split(',')
    categories = list(map(str.strip, categories))
    
    # Check if 'categories' key exists in user_data
    if 'categories' in user_data:
        user_data['categories'].extend(categories)
    else:
        user_data['categories'] = categories

    categoriesString = "\n".join(user_data['categories'])
    await update.message.reply_text(f'''Categories updated successfully!
Here are the updated categories:
{categoriesString}
''')
    return ConversationHandler.END

# Function to delete a category
async def deleteCategory(update: Update, context: CallbackContext):
    await update.message.reply_text("Please enter the category you want to delete: ")
    return DELETE_CATEGORY

# Function to handle deleting a category
async def handleDeleteCategory(update: Update, context: CallbackContext):
    category_to_delete = update.message.text.strip()
    
    if 'categories' in user_data and category_to_delete in user_data['categories']:
        user_data['categories'].remove(category_to_delete)
        await update.message.reply_text(f'Category "{category_to_delete}" deleted successfully!')
    else:
        await update.message.reply_text(f'Category "{category_to_delete}" not found.')

    return ConversationHandler.END

# Function to cancel the conversation
async def cancel(update: Update, context: CallbackContext):
    await update.message.reply_text("Operation canceled.")
    return ConversationHandler.END

# Conversation handler
conv_handler_editCategories = ConversationHandler(
    entry_points=[CommandHandler("editcategories", editCategories)],
    states={
        CATEGORY: [
            CommandHandler("addcategory", addCategories),
            CommandHandler("deletecategory", deleteCategory),
        ],
        ADD_NEW_CATEGORIES: [MessageHandler(~filters.COMMAND, handleAddCategories)],
        DELETE_CATEGORY: [MessageHandler(~filters.COMMAND, handleDeleteCategory)],
    },
    fallbacks=[CommandHandler("cancel", cancel)],
)
