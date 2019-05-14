import telebot
import parser

#main variables
TOKEN = "os.environ['TELEGRAM_TOKEN']"
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет, когда я вырасту, я буду.')
bot.polling()