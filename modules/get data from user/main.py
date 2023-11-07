import os
import json
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext
from helper import DATAENTRY

# Define states for the conversation
TYPE, CITY, STREET, HOUSE, FLOOR, METERING, RENOVATION, VERIFY = range(8)

# Initialize an empty dictionary to store user data
user_data = {}

# Create a dictionary to store user information (user_id as the key and user-specific data as the value)
users_info = {}

def start(update: Update, context: CallbackContext):
    # Start the data entry conversation from the helper code
    return DATAENTRY.start(update, context)

def main():
    # Your Telegram Bot API Token
    token = 'YOUR_TELEGRAM_BOT_TOKEN'

    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    # Create conversation handler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            TYPE: [MessageHandler(Filters.text & ~Filters.command, DATAENTRY.type)],
            CITY: [MessageHandler(Filters.text & ~Filters.command, DATAENTRY.city)],
            STREET: [MessageHandler(Filters.text & ~Filters.command, DATAENTRY.street)],
            HOUSE: [MessageHandler(Filters.text & ~Filters.command, DATAENTRY.house)],
            FLOOR: [MessageHandler(Filters.text & ~Filters.command, DATAENTRY.floor)],
            METERING: [MessageHandler(Filters.text & ~Filters.command, DATAENTRY.metering)],
            RENOVATION: [MessageHandler(Filters.text & ~Filters.command, DATAENTRY.renovation)],
            VERIFY: [MessageHandler(Filters.text & ~Filters.command, DATAENTRY.verify)],
        },
        fallbacks=[],
    )

    dp.add_handler(conv_handler)

    # Define a command to show the generated data
    def show_data(update: Update, context: CallbackContext):
        user = update.message.from_user
        user_id = user.id  # Get the user's Telegram user ID
        # user_data = users_info.get(user_id)

        try:
            # Retrieve all JSON files with the user's id in the filename
            generated_data = {}
            for filename in os.listdir():
                if filename.startswith(f"{user_id}_") and filename.endswith(".json"):
                    with open(filename, "r") as json_file:
                        data = json.load(json_file)
                        generated_data[filename] = data

            if generated_data:
                update.message.reply_text(json.dumps(generated_data, indent=4))
            else:
                update.message.reply_text("No generated data found.")
        except:
            update.message.reply_text("No user data found. Please start the conversation first.")

    dp.add_handler(CommandHandler('show_data', show_data))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
