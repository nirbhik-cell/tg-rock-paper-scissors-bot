from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import random

# Define a command handler function
def start(update: Update, context: CallbackContext) -> None:
    # Create a list of buttons
    button_list = [
        [InlineKeyboardButton("Rock", callback_data='rock')],
        [InlineKeyboardButton("Paper", callback_data='paper')],
        [InlineKeyboardButton("Scissors", callback_data='scissors')]
    ]

    # Create a reply markup with the button list
    reply_markup = InlineKeyboardMarkup(button_list)

    # Send a message with the button options
    update.message.reply_text('Choose your move:', reply_markup=reply_markup)

# Define a callback function for button presses
def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    user_choice = query.data

    # Generate a random choice for the bot
    bot_choice = random.choice(['rock', 'paper', 'scissors'])

    # Determine the winner
    result = determine_winner(user_choice, bot_choice)

    # Send the result to the user
    query.edit_message_text(text=f"You chose {user_choice}\nBot chose {bot_choice}\nResult: {result}")

def determine_winner(user_choice: str, bot_choice: str) -> str:
    # Determine the winner based on the choices
    if user_choice == bot_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'rock' and bot_choice == 'scissors') or
        (user_choice == 'paper' and bot_choice == 'rock') or
        (user_choice == 'scissors' and bot_choice == 'paper')
    ):
        return "You win!"
    else:
        return "Bot wins!"

def main() -> None:
    # Create an Updater object and set up the bot token
    updater = Updater(token='YOUR_BOT_TOKEN', use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the start command handler
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # Register the callback function for button presses
    button_handler = CallbackQueryHandler(button)
    dispatcher.add_handler(button_handler)

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
