import telebot
from telebot import types
bot = telebot.TeleBot
def get_cat(url):
    return url
@bot.message_handler(commands=['cat'])
def send_cat(message):
    url = get_cat('https://thecatapi.com')
    bot.reply_to(message, url)
if __name__ == '__main__':
    bot.polling(none_