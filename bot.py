import telebot
import parser

#main variables
TOKEN = "bot446260100:AAGH6JR31j2IMefwoW5zBph-P9zlT_lPHE4"
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет, когда я вырасту, я буду.')
bot.polling()