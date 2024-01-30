import telebot

bot = telebot.TeleBot('6464806247:AAGgPZQnv8fBwBMNL9cHvytuTVFiNXwISjE')



@bot.message_handler(commands=['start'])
def main(msg):
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    but1 = telebot.types.InlineKeyboardButton('First', callback_data='first')
    but2 = telebot.types.InlineKeyboardButton('Second', callback_data='second')
    markup.add(but1, but2)
    bot.send_message(msg.chat.id,'выбери кнопку:', reply_markup=markup)


@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'first':
            bot.send_message(call.message.chat.id, 'Ты человек')
        if call.data == 'second':
            bot.send_message(call.message.chat.id, 'Ты робот')


#ОБЯЗАТЕЛЬНО
bot.infinity_polling()
