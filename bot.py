from telegram.ext import Updater
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, MessageHandler, Filters
from abjad_generator import text2pdf
from os import environ

TOKEN = environ.get('TOKEN_FOR_ABJADPARSER_BOT')

updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

BOT_START_TEXT = """
Привет. Я перевожу текст в ноты используя библиотеку abjad

Для дополнительной информации посмотри сайт https://abjad.github.io/
""" 

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=BOT_START_TEXT)

def translate(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    text = update.message.text.lower()
    url_of_file = text2pdf(text)
    with open(url_of_file, 'rb') as file:
        context.bot.send_document(chat_id, document=file)

    

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

translate_handler = MessageHandler(Filters.text, translate)
dispatcher.add_handler(translate_handler)

updater.start_polling()

