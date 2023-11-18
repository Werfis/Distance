import telebot

bot = telebot.TeleBot()

@bot.message_handler(func=lambda message: True)
def repeat_message(message):
    bot.reply_to(message.chat.id, message.text)

bot.polling()
