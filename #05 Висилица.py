import telebot #Импортируем(подключаем) модуль с командами для телеграма
from random import randint #Подключаем функцию генерации случайных чисел


#Подключаемся к боту через его ТОКЕН
bot = telebot.TeleBot("1439408799:AAH6VxNNvXcrrtl3BcXUDDvnHEP3UhGBYCA")

word = "Антарктида"

#######  ОТВЕТ НА КОМАНДУ START
@bot.message_handler(commands = ['start']) #Ловим команду START
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Я хочу загадать слово.")


####### ОТВЕТ НА ТЕКСТОВОЕ СООБЩЕНИЕ
@bot.message_handler(content_types = ['text'])#Ловин новые текстовые сообщения
def otvet (message):

    letter = message.text
    if letter in word:
        bot.send_message(message.chat.id, "Такая буква есть")

bot.polling() #Запрос сообщения
