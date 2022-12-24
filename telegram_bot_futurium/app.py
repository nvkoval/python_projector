from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.updater import Updater
from telegram.ext.dispatcher import Dispatcher
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.filters import Filters

bot_token = '5905341866:AAEB13WoTNbjxxS61vNdFNJKGcriiKGkywg'
bot_user_name = "futurium_bot"

updater = Updater(bot_token, use_context=True)


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hey! Вітаємо у Futurium English School боті - \
        твоєму помічнику на шляху у вивченні англійської💛\
        Щоб ми могли вам краще допомогти - підкажіть нам ваш статус у школі ⬇️.\
        Please write /help to see the commands available.")


def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
    /price - To get the price URL
    /feedback - To get the GoogleForm URL """)


def price_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "This is a link to price\
            https://docs.google.com/spreadsheets/d/12EhBOVfDozZd3CHK5It6TBTkfvrdQrnlYK7EQITyYOs/edit#gid=1315899036")


def feedback_url(update: Update, context: CallbackContext):
    update.message.reply_text("Link to form for Feedback  =>\
    https://docs.google.com/forms/d/e/1FAIpQLSfHqJP-LqnfftURYlLoDw5kwSQWVGPhYSO59iBMLR80bjEVkA/viewform?usp=share_link")


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('feedback', feedback_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('price', price_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown))  # Filters out unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()