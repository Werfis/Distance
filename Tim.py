import telebot

bot = telebot.TeleBot("6480596150:AAGiVRMNtPO5ct_98aOMr3Ubww4FqXL-iCU")

@bot.message_handler(func=lambda message: True)
def repeat_message(message):
    bot.reply_to(message.chat.id, message.text)

bot.polling()