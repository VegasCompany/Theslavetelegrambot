#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple Bot to reply to Telegram messages
# This program is dedicated to the public domain under the CC0 license.
"""
This Bot uses the Updater class to handle the bot.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Job
import logging
import config
from functools import wraps
import os
import time
import sys

def restart(bot, update):
    bot.send_message(update.message.chat_id, "Bot is restarting...")
    time.sleep(0.2)
    os.execl(sys.executable, sys.executable, *sys.argv)

LIST_OF_ADMINS = [239288913, 346415768]

def restricted(func):
    @wraps(func)
    def wrapped(bot, update, *args, **kwargs):
        user_id = update.effective_user.id
        if user_id not in LIST_OF_ADMINS:
            print("Unauthorized access denied for {}.".format(user_id))
            return
        return func(bot, update, *args, **kwargs)
    return wrapped
	

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    update.message.reply_text('Hi!')
    custom_keyboard = [['top-left', 'top-right'], ['bottom-left', 'bottom-right']]
    reply_markup = bot.ReplyKeyboardMarkup(custom_keyboard)
    bot.send_message(chat_id=chat_id, text="Custom Keyboard Test", reply_markup=reply_markup)



def help(bot, update):
    update.message.reply_text('Help!')
	
@restricted
def getkeepass(bot, update):
    chat_id = update.message.chat_id
    bot.send_document(chat_id=chat_id, document=open('\\\\srv-file\\it\\zlo\\FindMe.kdbx', 'rb'))
	
def password(bot, update, args, job_queue, chat_data):
	chat_id = update.message.chat_id
	try:
		due = int(args[0])
		if due == 9966996699:
			update.message.reply_text('YfljtkjDdjlbnmGfhjkm')
		else:
			update.message.reply_text('Provalivai')
	except (IndexError, ValueError):
		update.message.reply_text('Error')

def echo(bot, update):
    update.message.reply_text(update.message.text)


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(config.token)

    # Get the dispatcher to register handlers
    bot = updater.dispatcher

    # on different commands - answer in Telegram
    bot.add_handler(CommandHandler("start", start))
    bot.add_handler(CommandHandler("help", help))
    bot.add_handler(CommandHandler("getkeepass", getkeepass))
    bot.add_handler(CommandHandler("password", password, pass_args=True, pass_job_queue=True, pass_chat_data=True))

    # on noncommand i.e message - echo the message on Telegram
    bot.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    bot.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()