import telebot
import bs4

#main variables
TOKEN = "bot446260100:AAGH6JR31j2IMefwoW5zBph-P9zlT_lPHE4"
bot = telebot.TeleBot(token=TOKEN)
#handlers
@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет, когда я вырасту, я буду.')

@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    if text == "привет":
        bot.send_message(chat_id, 'Привет, я бот - парсер.')
    elif text == "как дела?":
        bot.send_message(chat_id, 'Хорошо, а у тебя?')
    else:
        bot.send_message(chat_id, 'Простите, я вас не понял :(')

bot.polling()