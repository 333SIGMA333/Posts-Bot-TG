import telebot
from telebot import types



# Создание Telegram-бота
bot = telebot.TeleBot('6323112005:AAFn6M_9NV5SC62qErK7f-5RBN1atI6XNX0')

# Органичение доступа к боту по ID
users = [1065209033]
@bot.message_handler(func=lambda message: message.chat.id not in users)
def some(message):
    bot.send_message(message.chat.id, 'Извините, Создатели не разрешают мне общаться с незнакомыми пользователями')






@bot.message_handler(commands=['start'])
def post(message):
    bot.send_message(message.chat.id, 'Пришли фотку/текст и жми "Запостить"')
    


@bot.message_handler(content_types=['photo'], func=lambda message: True)
def photo_handler(message):
    # Создание кнопки "заказать"
    button = types.InlineKeyboardButton('Заказать', url='https://t.me/nupodymym_bot?start=bot_chanel')
    global keyboard
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(button)


    global photo
    photo = message.photo[-1].file_id
    global caption
    caption = message.caption
    # bot.send_photo(-1001521471400, photo_id, reply_markup=keyboard)

    # Кнопки после сообщения
    markup = types.InlineKeyboardMarkup()
    button_napechatat = types.InlineKeyboardButton(text = 'Запостить', callback_data="Order")
    markup.row(button_napechatat)

    if message:
        # Отправляю приветственный текст
        bot.send_message(message.chat.id, 'Пришли фотку/текст и жми "Запостить"',  reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Пришли фотку/текст и жми "Запостить"', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def Handler(CallBack):
    if CallBack.data == 'Order':
        bot.send_photo(-1001521471400, photo, caption, reply_markup=keyboard)   








# Запуск бота
while True:
    try: bot.polling(none_stop=True)
    except Exception as ex: print (ex)
