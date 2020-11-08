import telebot

bot = telebot.TeleBot("1439408799:AAH6VxNNvXcrrtl3BcXUDDvnHEP3UhGBYCA")

last_message = "Приветствую"

@bot.message_handler(commands = ['start']) #Ловим команду старт
def start_massage(message):
    bot.send_message(message.chat.id, "Привет, зачем ты меня позвал?") #Ответочка команде START

@bot.message_handler(commands=['photo']) #Ловим команду PHOTO
def send_pictures(message):
    with open("329966_original.jpg", 'rb') as Vinny: #Загружаем картинку
        bot.send_photo(message.chat.id, Vinny) #Шлем фото Винни

@bot.message_handler(content_types = ['text'])#Ловин новые текстовые сообщения
def otvet (message):
    print(message.from_user)
    global last_message
    bot.send_message(message.chat.id, message.from_user.first_name +", " + last_message)
    last_message = message.text


bot.polling()
