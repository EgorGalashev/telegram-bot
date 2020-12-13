import telebot #Импортируем(подключаем) модуль с командами для телеграма.
from random import randint #Подключаем функцию генерации случайных чисел.


#Подключаемся к боту через его ТОКЕН.
bot = telebot.TeleBot("1439408799:AAH6VxNNvXcrrtl3BcXUDDvnHEP3UhGBYCA")


animals = ["тигр", "леопард"]
geography = ["африка","америка"]
space = ['скафандр', 'луна']
other = ["антарктида", "параллелепипед", "акваланг", "пылесос", "кораблекрушение"]

word = None

letters = []
not_guessed = []


#########  ОТВЕТ НА КОМАНДУ START
@bot.message_handler(commands=['start'])  # Ловим команду START
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Животные', callback_data=1))
    markup.add(telebot.types.InlineKeyboardButton(text='География', callback_data=2))
    markup.add(telebot.types.InlineKeyboardButton(text='Космос', callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(text='Разное', callback_data=4))
    bot.send_message(message.chat.id, text="Привет! Давай сыграем в виселицу, я хочу загадать слово, выбери тему: ",
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    # bot.answer_callback_query(callback_query_id=call.id, text='Спасибо за честный ответ!')

    if call.data == '1':
        words = animals

    elif call.data == '2':
        words = geography

    elif call.data == '3':
        words = space

    elif call.data == '4':
        words = other

    global word
    word = words[randint(0, len(words) - 1)]


    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    bot.send_message(call.message.chat.id, "Я загадал слово, в нём " + str(len(word)) + " букв. Попробуй его угадать!")


######## OТВЕТ НА ТЕКСТОВОЕ СООБЩЕНИЕ
@bot.message_handler(content_types=['text'])  # Ловим сообщения с текстом
def otvet(message):
    print(message.text)
    letter = message.text.lower()

    if len(letter) == 1:  # Если прислали 1 букву
        if letter in word:
            bot.send_message(message.chat.id, "Такая буква есть")
            letters.append(letter)  # Добавим  букву в список угаданных букв

        else:
            bot.send_message(message.chat.id, "Нет такой буквы")
            # Добавляем букву в спиок неугаданных

    else:  # Если прислали целое слово
        if letter == word:
            bot.send_message(message.chat.id, "Дааааа! Ты угадал!")
            return
        else:
            bot.send_message(message.chat.id, "Не угадал!")


    prompt = ''
    quessed = True
    for l in word:
        if l in letters:
            prompt += l
        else:
            prompt += "🔴"
            quessed = False

    if quessed == True:
        bot.send_message(message.chat.id, 'URAA!')

    bot.send_message(message.chat.id, prompt)
    if len(not_guessed) > 0:
        bot.send_message(message.chat.id, not_guessed)


bot.polling()  # Запрос сообщений
