import telebot
from telebot import types


# bot = telebot.TeleBot('6385680785:AAGluazz4qNCLr4R98_YEpOhuGEb-1-qmm4')
# @bot.message_handler(commands=['start'])
# def main(message):
# markup = types.ReplyKeyboardMarkup()
# btn1 = types.KeyboardButton('Узнать котировки')
# btn2 = types.KeyboardButton('Прочитать новости')
# btn3 = types.KeyboardButton('Прочитать аналитические статьи')
# markup.row(btn1, btn2)
# markup.row(btn3)
# bot.send_message(message.chat.id, "Какое действие выполнить?", reply_markup=markup)
# bot.register_next_step_handler(message, action1)

def mainfortest(message):
    if message == "/start":
        return ["Какое действие выполнить",'Узнать котировки', 'Прочитать новости', 'Прочитать аналитические статьи']
    return None
