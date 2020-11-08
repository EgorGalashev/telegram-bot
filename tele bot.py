import telebot

bot = telebot.TeleВot("1439408799:AAH6VxNNvXcrrtl3BcXUDDvnHEP3UhGBYCA")

@bot.massage_handler(commands = ['start'])
def start_massage(massage):
    bot.send_message(message.chat.id, "Привет, зачем ты меня позвал?")


bot.polling()
