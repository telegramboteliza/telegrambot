import telebot
bot = telebot.TeleBot('1120622193:AAFnEMCqK0irzYbSpH0cdPqbBLEuTZIcxIQ')
import sqlite3


# Подключаем модуль случайных чисел
import random

# Подключаем модуль для Телеграма

import telebot

# Импортируем типы из модуля, чтобы создавать кнопки

from telebot import types

# Заготовки для трёх предложений

first = ["лера не выйбывайся я занят"]

second = ["лера не выйбывайся я занят"]

second_add = ["лера не выйбывайся я занят"]

third = ["лера не выйбывайся я занят"]


# Метод, который получает сообщения и обрабатывает их

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «Привет»

    if message.text == "Привет":

        # Пишем приветствие

        bot.send_message(message.from_user.id, "Привет, сейчас я расскажу тебе гороскоп на сегодня.")

        # Готовим кнопки

        keyboard = types.InlineKeyboardMarkup()

        # По очереди готовим текст и обработчик для каждого знака зодиака

        key_oven = types.InlineKeyboardButton(text='Овен', callback_data='zodiac')

        # И добавляем кнопку на экран

        keyboard.add(key_oven)

        key_telec = types.InlineKeyboardButton(text='Телец', callback_data='zodiac')

        keyboard.add(key_telec)

        key_bliznecy = types.InlineKeyboardButton(text='Близнецы', callback_data='zodiac')

        keyboard.add(key_bliznecy)

        key_rak = types.InlineKeyboardButton(text='Рак', callback_data='zodiac')

        keyboard.add(key_rak)

        key_lev = types.InlineKeyboardButton(text='Лев', callback_data='zodiac')

        keyboard.add(key_lev)

        key_deva = types.InlineKeyboardButton(text='Дева', callback_data='zodiac')

        keyboard.add(key_deva)

        key_vesy = types.InlineKeyboardButton(text='Весы', callback_data='zodiac')

        keyboard.add(key_vesy)

        key_scorpion = types.InlineKeyboardButton(text='Скорпион', callback_data='zodiac')

        keyboard.add(key_scorpion)

        key_strelec = types.InlineKeyboardButton(text='Стрелец', callback_data='zodiac')

        keyboard.add(key_strelec)

        key_kozerog = types.InlineKeyboardButton(text='Козерог', callback_data='zodiac')

        keyboard.add(key_kozerog)

        key_vodoley = types.InlineKeyboardButton(text='Водолей', callback_data='zodiac')

        keyboard.add(key_vodoley)

        key_ryby = types.InlineKeyboardButton(text='Рыбы', callback_data='zodiac')

        keyboard.add(key_ryby)

        # Показываем все кнопки сразу и пишем сообщение о выборе

        bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)

    elif message.text == "/help":

        bot.send_message(message.from_user.id, "Напиши Привет")

    else:

        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


# Обработчик нажатий на кнопки

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # Если нажали на одну из 12 кнопок — выводим гороскоп

    if call.data == "zodiac":
        # Формируем гороскоп

        msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(
            second_add) + ' ' + random.choice(third)

        # Отправляем текст в Телеграм

        bot.send_message(call.message.chat.id, msg)

connection = sqlite3.connect("database", check_same_thread = True)
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Inventory_on (ID INT, 'Primary weapon' TEXT, 'Secondary weapon' TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS Clans (Name TEXT, Points INT)")
cursor.execute("CREATE TABLE IF NOT EXISTS WorkStatus (ID INT, Status INT)")

connection.commit()
connection.close()


# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)