from telegram.ext import Updater
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, MessageHandler, Filters
from abjad_generator import text2pdf
from bot_texts import hello_text
from sys import argv
import Constants
import pdb

try:
    TOKEN = argv[1]
except IndexError:
    TOKEN = input("ENTER BOT TOKEN: ")

updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=hello_text)

def translate(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    text = update.message.text.lower()
    url_of_file = text2pdf(text)
    with open(url_of_file, 'rb') as file:
        context.bot.send_document(chat_id, document=file)


# def print_update(update: Update, context: CallbackContext):
#     print(update)
    

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

translate_handler = MessageHandler(Filters.text, translate)
dispatcher.add_handler(translate_handler)

# update_printer = MessageHandler(Filters.all, print_update)
# dispatcher.add_handler(update_printer)

updater.start_polling()

