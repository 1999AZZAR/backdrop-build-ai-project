import json
import random
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext

# Define states for the conversation
TYPE, CITY, STREET, HOUSE, FLOOR, METERING, RENOVATION, VERIFY = range(8)

# Initialize an empty dictionary to store user data
user_data = {}

# Create a dictionary to store user information (user_id as the key and user-specific data as the value)
users_info = {}

class DATAENTRY:

    @staticmethod
    # Define a function to start the conversation
    def start(update: Update, context: CallbackContext):
        user = update.message.from_user
        user_id = user.id  # Get the user's Telegram user ID
        users_info[user_id] = {}  # Create an empty dictionary for the user's data
        keyboard = [[KeyboardButton("Secondary-Beta"), KeyboardButton("New Buildings")]]
        reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
        update.message.reply_text(
            f"Hi, {user.first_name}! I am PAR, personal realtor analyst. "
            "Let's start by gathering some information.",
            reply_markup=reply_markup,
        )
        return TYPE

    # Define functions for each step of the conversation
    def type(update: Update, context: CallbackContext):
        user = update.message.from_user
        user_id = user.id  # Get the user's Telegram user ID
        user_data = users_info[user_id]  # Get the user's data dictionary
        user_data['PropertyType'] = update.message.text
        update.message.reply_text(
            "Please enter the city:",
            reply_markup={"keyboard": [], "remove_keyboard": True},
        )
        return CITY

    def city(update: Update, context: CallbackContext):
        user = update.message.from_user
        user_id = user.id  # Get the user's Telegram user ID
        user_data = users_info[user_id]  # Get the user's data dictionary
        user_data['City'] = update.message.text
        update.message.reply_text("Please enter the street:")
        return STREET

    def street(update: Update, context: CallbackContext):
        user = update.message.from_user
        user_id = user.id  # Get the user's Telegram user ID
        user_data = users_info[user_id]  # Get the user's data dictionary
        user_data['Street'] = update.message.text
        update.message.reply_text("Please enter the house number:")
        return HOUSE

    def house(update: Update, context: CallbackContext):
        user = update.message.from_user
        user_id = user.id  # Get the user's Telegram user ID
        user_data = users_info[user_id]  # Get the user's data dictionary
        user_data['House'] = update.message.text
        update.message.reply_text("Please enter the floor number:")
        return FLOOR

    def floor(update: Update, context: CallbackContext):
        user = update.message.from_user
        user_id = user.id  # Get the user's Telegram user ID
        user_data = users_info[user_id]  # Get the user's data dictionary
        user_data['Floor'] = update.message.text
        update.message.reply_text("Please enter the metering of the apartment:")
        return METERING

    def metering(update: Update, context: CallbackContext):
        user = update.message.from_user
        user_id = user.id  # Get the user's Telegram user ID
        user_data = users_info[user_id]  # Get the user's data dictionary
        user_data['Metering_Apartments'] = update.message.text
        keyboard = [["No", "Renovation", "Cosmetic", "Designer"]]
        reply_markup = {"keyboard": keyboard, "one_time_keyboard": True}
        update.message.reply_text(
            "Please select the type of renovation:",
            reply_markup=reply_markup,
        )
        return RENOVATION

    def renovation(update: Update, context: CallbackContext):
        user = update.message.from_user
        user_id = user.id  # Get the user's Telegram user ID
        user_data = users_info[user_id]  # Get the user's data dictionary
        user_data['Renovation'] = update.message.text
        keyboard = [["Yes", "No"]]
        reply_markup = {"keyboard": keyboard, "one_time_keyboard": True}
        data_to_verify = "Please verify the following data:\n\n" + "\n".join(
            f"{key}: {value}" for key, value in user_data.items()
        )
        update.message.reply_text(
            data_to_verify,
            reply_markup=reply_markup,
        )
        return VERIFY

    def verify(update: Update, context: CallbackContext):
        user = update.message.from_user
        user_id = user.id  # Get the user's Telegram user ID
        user_data = users_info[user_id]  # Get the user's data dictionary

        if update.message.text.lower() == "yes":
            # Generate a random number and assign it to the filename
            Number = f"{user_id}_{random.randint(1000, 9999)}.json"

            # Save the data to a JSON file
            with open(Number, "w") as json_file:
                json.dump(user_data, json_file, indent=4)

            update.message.reply_text(
                "Data has been saved. Here is the generated dataset:",
                reply_markup={"keyboard": [], "remove_keyboard": True},
            )
            update.message.reply_text(json.dumps(user_data, indent=4)
            +"\nPlease use the '/show_data' command to view your generated data.")
        else:
            # If the user wants to correct data, start from the beginning
            update.message.reply_text(
                "Let's correct the data. Please enter the city:",
                reply_markup={"keyboard": [], "remove_keyboard": True},
            )
            return TYPE

        return ConversationHandler.END
