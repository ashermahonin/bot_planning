import telebot
from telebot import types

bot = telebot.TeleBot('MYTOKEN')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Мои встречи", url='https://outlook.live.com/owa/')) #first need to use API og google or outlook 
    markup.add(types.InlineKeyboardButton("Создать встречу", url='https://calendar.google.com/calendar/u/0/r?pli=1'))
    bot.send_message(message.chat.id, '<b>Что вы хотите сделать?</b>', reply_markup=markup,  parse_mode='html')
#inlinekeyboard can use for create url-button
@bot.message_handler(commands=['start'])
def start_2(message):
    markup = types.ReplyKeyboardMarkup()
    my_meets = types.KeyboardButton('Мои встречи')
    create_meets = types.KeyboardButton('Создать встречу')
    markup.add(my_meets, create_meets)
    bot.send_message(message.chat.id, 'Что вы хотите сделать?', reply_markup=markup)

#@bot.message_handler(commands=[])
#just draft
