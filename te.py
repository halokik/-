import telebot

bot = telebot.TeleBot("7258082736:AAEof4V0c7vGL5ZlOboQ-PKjZCuftB4Dzag")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()