import telebot


bot = telebot.TeleBot("753047949:AAG-W93ECezUVequDti4jXJcHWAO_OcWuvA")

@bot.message_handler(commands=['Start'])
def send_welcome(message):
	bot.reply_to(message, "Hello")
@bot.message_handler(commands=['hello'])
def send_welcome(message):
	bot.reply_to(message, "How was your day")
@bot.message_handler(commands=['My day was good'])
def send_welcome(message):
	bot.reply_to(message, "Good")
	
@bot.message_handler(commands=['bye'])
def send_welcome(message):
	bot.reply_to(message, "Bye")
	

	

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()
