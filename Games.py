import telebot #Импортируем(подключаем) модуль с командами для телеграма
from random import randint #Подключаем функцию генерации случайных чисел


#Подключаемся к боту через его ТОКЕН
bot = telebot.TeleBot("1439408799:AAH6VxNNvXcrrtl3BcXUDDvnHEP3UhGBYCA")


random_number = 0 #Число которое потом заменится на случайное
counter = 0 #


#######  ОТВЕТ НА КОМАНДУ START
@bot.message_handler(commands = ['start']) #Ловим команду START
def start_massage(message):
    global random_number #Разрешаем функции start_message менять переменную random_number
    bot.send_message(message.chat.id, "Привет, зачем ты меня позвал?") #Ответочка команде START
    random_number = randint(0, 100) #ГЕНЕРАЦИЯ случайного числа


####### ОТВЕТ НА ТЕКСТОВОЕ СООБЩЕНИЕ
@bot.message_handler(content_types = ['text'])#Ловин новые текстовые сообщения
def otvet (message):
    global counter # Разрешаем менять глобальную переменную counter
    try: #Попытайся сделать что-то
        user_number =int (message.text) #Превращаем ответ пользователя из строки(str) число(int)

        counter += 1 # Пребавляем 1 к переменной counter
        
        if user_number == random_number:
            bot.send_message(message.chat.id, "You quessed!")
        
        elif user_number > random_number:
            bot.send_message(message.chat.id, "Too big")
            
        
        elif user_number < random_number:
            bot.send_message(message.chat.id, "Too small")

        else:
            bot.send_message(message.chat.id, str(random_number)+ " Я загадал это число")


    except:
        bot.send_message(message.chat, "WROOONG! ONLY NUMBERS")



    #bot.send_message(message.chat.id, random_number)


bot.polling() #Запрос сообщений
