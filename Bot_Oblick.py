"""
    библиотека telebot необходима для взаимодействия с API телеграмм-бота
    types необходим для создания таблиц и кнопок внутри сообщений телеграмм-бота
    requests необходимы для запроса кода интернет страницы
    bs4 необходим для работы с html кодом интернет страницы
"""
import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup

"""
    Используем токен телеграмм-бота при помощи библиотеки telebot
"""
bot = telebot.TeleBot('6385680785:AAGluazz4qNCLr4R98_YEpOhuGEb-1-qmm4')

"""
    Записываем в callback необходимые пользователю действия. В dict_link храним частицы ссылки на страницу ценной бумаги
"""

callback1 = ''
callback2 = ''
callback3 = ''

dict_link = {
    "Доллар": "currencies/usd-rub",
    "Евро": "currencies/eur-rub",
    "Фунт": "currencies/gbp-rub",
    "Юань": "currencies/cny-rub",
    "Сбер": "equities/sberbank_rts",
    "ВТБ": "equities/vtb_rts",
    "Тинькофф": "equities/tcs-group-holding-plc?cid=1153662",
    "Совкомбанк": "novalue",
    "Московская биржа": "equities/moskovskaya-birzha-oao",
    "Спб биржа": "equities/spb-birzha-pao",

}


@bot.message_handler(commands=['start'])
def main(message):
    """
        :param message: command start from user
        :type message: class 'telebot.types.Message'
        После команды /start предлагает пользователю выбрать траекторию работы с ботом,
        отправляя пользователю сообщение с тремя встроенными в клавиатуру кнопками
        :returns: -
        :rtype: -
    """
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Узнать котировки')
    btn2 = types.KeyboardButton('Прочитать новости')
    btn3 = types.KeyboardButton('Прочитать аналитические статьи')
    markup.row(btn1, btn2)
    markup.row(btn3)
    bot.send_message(message.chat.id, "Какое действие выполнить?", reply_markup=markup)
    bot.register_next_step_handler(message, action1)


def action1(message):
    """
        :param message: message from user
        :type message: class 'telebot.types.Message'
        :globals: callback1, callback2, callback3
        После выбора требуемого действия предлагает пользователю выбрать сектор рынка,
        к которому необходимо применить действие. Отправляет сообщение
        :returns: -
        :rtype: -
    """
    global callback1, callback2, callback3
    callback1 = message.text
    if message.text == 'Узнать котировки' or message.text == 'Прочитать новости' or message.text == 'Прочитать ' \
                                                                                                    'аналитические ' \
                                                                                                    'статьи':
        markup1 = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Банковский сектор')
        btn2 = types.KeyboardButton('Валюты')
        markup1.row(btn1, btn2)
        bot.send_message(message.chat.id, "Какой сектор рынка интересует?", reply_markup=markup1)
        bot.register_next_step_handler(message, action2)
    else:
        bot.send_message(message.chat.id, "Я вас не понимаю, начните операцию с функцией /start заново")


def action2(message):
    """
        :param message: message from user
        :type message: class 'telebot.types.Message'
        :globals: callback1, callback2, callback3
        После выбора требуемого сектора рынка предлагает пользователю выбрать наименование ценной бумаги,
        к которой необходимо применить действие. Отправляет сообщение
        :returns: -
        :rtype: -
    """
    global callback1, callback2, callback3
    callback2 = message.text
    markup2 = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Доллар')
    btn2 = types.KeyboardButton('Евро')
    btn3 = types.KeyboardButton('Фунт')
    btn4 = types.KeyboardButton('Юань')
    markup2.row(btn1, btn2)
    markup2.row(btn3, btn4)
    markup3 = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Сбер')
    btn2 = types.KeyboardButton('ВТБ')
    btn3 = types.KeyboardButton('Тинькофф')
    btn4 = types.KeyboardButton('Совкомбанк')
    btn5 = types.KeyboardButton('Московская биржа')
    btn6 = types.KeyboardButton('Спб биржа')
    markup3.row(btn1, btn2)
    markup3.row(btn3, btn4)
    markup3.row(btn5, btn6)
    if message.text == 'Валюты':
        bot.send_message(message.chat.id, "Выберите валюту", reply_markup=markup2)
        bot.register_next_step_handler(message, action3)
    elif message.text == 'Банковский сектор':
        bot.send_message(message.chat.id, "Выберите акцию", reply_markup=markup3)
        bot.register_next_step_handler(message, action3)
    else:
        bot.send_message(message.chat.id, "Я вас не понимаю, начните операцию с функцией /start заново")


def news(name):
    """
        :param name: name of security investment
        :type name: str
        :returns: 3 titles, links and links on images in category news and
        3 titles, links and links on images in category analysis
        :rtype: list
    """
    link_part = "https://ru.investing.com/search/?q=" + name.replace(' ', '%20') + "&tab=news"
    r = requests.get(link_part)
    src = r.text
    soup = BeautifulSoup(src, "lxml")

    all_article_dives = soup.find_all("div", {"class": "articleItem"})
    all_article_titles = [div.find("a", {"class": "title"}).text for div in all_article_dives]
    all_article_titles = [t for t in all_article_titles if t != "{{title}}"]
    all_texts = []
    title_link = 0
    for link in all_article_dives:
        for p in link.find_all('a', href=True):
            if p['href'] != "{{link}}":
                title_link += 1
                if title_link % 2 == 0:
                    all_texts += [
                        str("[" + all_article_titles[title_link // 2 - 1] + "]" + "(https://ru.investing.com/" + p[
                            'href'] + ")")]
    for j in all_article_dives:
        for p in j.find_all('img', src=True):
            if p['src'] != "{{image}}":
                all_texts += [p['src']]
    return all_texts


def photo(link):
    """
        :param link: link on image
        :type link: str
        По ссылке функция получает картинку, сохраненную в image_name.jpg
        :returns: image
        :rtype: image
    """
    img_data = requests.get(link).content
    with open('image_name.jpg', 'wb') as handler:
        handler.write(img_data)
    return img_data


def equities(name):
    """
        :param name: piece of link on security investment
        :type name: str
        :returns: the price of the security
        :rtype: str
    """
    link_part = "https://ru.investing.com/" + name
    r = requests.get(link_part)
    src = r.text
    soup = BeautifulSoup(src, "lxml")
    kot_dives = soup.find("div", {"class": "flex flex-wrap gap-x-4 gap-y-2 items-center md:gap-6 mb-3 md:mb-0.5"})
    return kot_dives.text.replace('+', '\n+', 1).replace("(", " (").replace('-', '\n-', 1)


def currencies(name):
    """
        :param name: piece of link on currency
        :type name: str
        :returns: the price of the currency
        :rtype: str
    """
    link_part = "https://ru.investing.com/" + name
    r = requests.get(link_part)
    src = r.text
    soup = BeautifulSoup(src, "lxml")
    kot_dives = soup.find("div",
                          {"class": "instrument-price_instrument-price__2w9MW flex items-end flex-wrap font-bold"})
    return kot_dives.text.replace('+', '\n+', 1).replace("(", " (").replace('-', '\n-', 1)


def action3(message):
    """
        :param message: message from user
        :type message: class 'telebot.types.Message'
        :globals: callback1, callback2, callback3, dict_link
        После выбора требуемого наименования ценной бумаги выполняет запрос на сайт Investing.com с помощью
        функций news, currencies, equities получает требуемые данные (текст заголовка, ссылка на статью, ссылка на фото
         или цену ценной бумаги с информацией о ее изменении за последний торговый день). Отправляет сообщение
        :returns: -
        :rtype: -
    """
    global callback1, callback2, callback3, dict_link
    callback3 = message.text
    bot.send_message(message.chat.id, "Выполняю запрос...")
    if callback3 in dict_link.keys():
        texts = news(message.text)
    else:
        bot.send_message(message.chat.id, "Я вас не понимаю, начните операцию с функцией /start заново")
        return

    if callback1 == 'Прочитать новости':
        for i in range(0, 3):
            file = photo(texts[i + 6])
            bot.send_photo(message.chat.id, file, texts[i], parse_mode='Markdown')
        bot.send_message(message.chat.id, "Нажмите на /start чтобы сделать новый запрос")

    elif callback1 == 'Прочитать аналитические статьи':
        for i in range(3, 6):
            if i == 3:
                file = photo("https://dewiar.net/wp-content/uploads/2022/10/Analitika-umnoj-upakovki.jpg")
            elif i == 4:
                file = photo("https://marketingsquare.co.uk/wp-content/uploads/2017/04/shutterstock_532721611.jpg")
            else:
                file = photo(
                    "https://static.tildacdn.com/tild3537-3132-4135-b263-623836626239/shutterstock_4316669.jpg")
            bot.send_photo(message.chat.id, file, texts[i], parse_mode='Markdown')
        bot.send_message(message.chat.id, "Нажмите на /start чтобы сделать новый запрос")
    elif callback1 == 'Узнать котировки':
        name = dict_link[callback3]
        if name[:10] == "currencies":
            value = currencies(name)
            if "+" in value:
                file = photo("https://i01.fotocdn.net/s128/0b31e3f9c2feaf9c/gallery_xl/2899005306.jpg")
            else:
                file = photo("https://www.cointribune.com/app/uploads/2019/09/loss-1.jpg")
            bot.send_photo(message.chat.id, file, value)

        elif name[:8] == "equities":
            value = equities(name)
            if "+" in value:
                file = photo("https://i01.fotocdn.net/s128/0b31e3f9c2feaf9c/gallery_xl/2899005306.jpg")
            else:
                file = photo("https://www.cointribune.com/app/uploads/2019/09/loss-1.jpg")
            bot.send_photo(message.chat.id, file, value)
        elif name[:10] == "novalue":
            value = "IPO компании скоро начнётся. Цена размещения составит от 10,50 до 11,50 руб. за акцию, исходя из "\
                    "чего свою рыночную капитализацию банк оценил в сумме от 200 до 219 млрд руб"
            file = photo("https://i01.fotocdn.net/s128/0b31e3f9c2feaf9c/gallery_xl/2899005306.jpg")
            bot.send_photo(message.chat.id, file, value)
        bot.send_message(message.chat.id, "Нажмите на /start чтобы сделать новый запрос")


"""
    Используем функцию bot.polling для непрерывной работы бота
"""
bot.polling(none_stop=True)
