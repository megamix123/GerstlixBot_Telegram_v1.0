import telebot
from telebot import types
from gerstlix_python import gerstlixAPI
from dotenv import load_dotenv
import os
load_dotenv()

TELEGRAM_TOCKEN=(os.getenv('TELEGRAM_TOCKEN'))
GERSTLIX_TOCKEN=(os.getenv('GERSTLIX_TOCKEN'))



bot = telebot.TeleBot(TELEGRAM_TOCKEN)
kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
gx = gerstlixAPI(token=GERSTLIX_TOCKEN)
ADMIN_IDS = 807760971

@bot.message_handler(func = lambda message: message.text == "Назад")
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет!\n Если ты нашёл баг или у тебя есть предложение по улучшению бота то обязательно сообщи нам, через команду /feedback *text*")
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    co = types.KeyboardButton(text="Центральный Округ")
    uo = types.KeyboardButton(text="Южный Округ")
    so = types.KeyboardButton(text="Северный Округ")
    vo = types.KeyboardButton(text="Восточный Округ")
    zo = types.KeyboardButton(text="Западный Округ")
    po = types.KeyboardButton(text="Приморский Округ")
    fo = types.KeyboardButton(text="Федеральный Округ")
    kb.add(co, uo, so, vo, zo, po, fo)
    bot.send_message(message.chat.id, "Выберите сервер:", reply_markup=kb)

###################################################################################
@bot.message_handler(func = lambda message: message.text == "Центральный Округ")
def razd(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    adm = types.KeyboardButton(text="Следящая администрация[ЦО]")
    led = types.KeyboardButton(text="Лидеры[ЦО]")
    dep = types.KeyboardButton(text="Заместители[ЦО]")
    nazad = types.KeyboardButton(text="Назад")
    kb.add(adm, led, dep, nazad)
    bot.send_message(message.chat.id, "Выберите интересующий пункт:", reply_markup=kb)

@bot.message_handler(func = lambda message: message.text == "Южный Округ")
def razd(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    adm = types.KeyboardButton(text="Следящая администрация[ЮО]")
    led = types.KeyboardButton(text="Лидеры[ЮО]")
    dep = types.KeyboardButton(text="Заместители[ЮО]")
    nazad = types.KeyboardButton(text="Назад")
    kb.add(adm, led, dep, nazad)
    bot.send_message(message.chat.id, "Выберите интересующий пункт:", reply_markup=kb)

@bot.message_handler(func = lambda message: message.text == "Северный Округ")
def razd(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    adm = types.KeyboardButton(text="Следящая администрация[СО]")
    led = types.KeyboardButton(text="Лидеры[СО]")
    dep = types.KeyboardButton(text="Заместители[СО]")
    nazad = types.KeyboardButton(text="Назад")
    kb.add(adm, led, dep, nazad)
    bot.send_message(message.chat.id, "Выберите интересующий пункт:", reply_markup=kb)

@bot.message_handler(func = lambda message: message.text == "Восточный Округ")
def razd(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    adm = types.KeyboardButton(text="Следящая администрация[ВО]")
    led = types.KeyboardButton(text="Лидеры[ВО]")
    dep = types.KeyboardButton(text="Заместители[ВО]")
    nazad = types.KeyboardButton(text="Назад")
    kb.add(adm, led, dep, nazad)
    bot.send_message(message.chat.id, "Выберите интересующий пункт:", reply_markup=kb)

@bot.message_handler(func = lambda message: message.text == "Западный Округ")
def razd(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    adm = types.KeyboardButton(text="Следящая администрация[ЗО]")
    led = types.KeyboardButton(text="Лидеры[ЗО]")
    dep = types.KeyboardButton(text="Заместители[ЗО]")
    nazad = types.KeyboardButton(text="Назад")
    kb.add(adm, led, dep, nazad)
    bot.send_message(message.chat.id, "Выберите интересующий пункт:", reply_markup=kb)

@bot.message_handler(func = lambda message: message.text == "Приморский Округ")
def razd(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    adm = types.KeyboardButton(text="Следящая администрация[ПО]")
    led = types.KeyboardButton(text="Лидеры[ПО]")
    dep = types.KeyboardButton(text="Заместители[ПО]")
    nazad = types.KeyboardButton(text="Назад")
    kb.add(adm, led, dep, nazad)
    bot.send_message(message.chat.id, "Выберите интересующий пункт:", reply_markup=kb)

@bot.message_handler(func = lambda message: message.text == "Федеральный Округ")
def razd(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    adm = types.KeyboardButton(text="Следящая администрация[ФО]")
    led = types.KeyboardButton(text="Лидеры[ФО]")
    dep = types.KeyboardButton(text="Заместители[ФО]")
    nazad = types.KeyboardButton(text="Назад")
    kb.add(adm, led, dep, nazad)
    bot.send_message(message.chat.id, "Выберите интересующий пункт:", reply_markup=kb)
###################################################################################



###################################################################################
@bot.message_handler(func = lambda message: message.text == "Следящая администрация[ЦО]")   
def coadm(message):
    bot.send_message(message.chat.id, "В разработке...")
@bot.message_handler(func = lambda message: message.text == "Лидеры[ЦО]")
def coled(message):
    bot.send_message(message.chat.id, "Ожидаем ответа API....")
    data = gx.get_leaders(server=201)
    bot.send_message(message.chat.id, "Формируем ответ....")
    if data["success"]:
        players = data['data']['players']
        result = ""
        for i in players:
            if i['fraction'] == 1:fraction_name = "Городская Полиция"
            elif i['fraction'] == 2:fraction_name = "Окружная полиция"
            elif i['fraction'] == 3:fraction_name = "Городская Больница"
            elif i['fraction'] == 4:fraction_name = "Правительство"
            elif i['fraction'] == 5:fraction_name = "Центр Лицензирования"
            elif i['fraction'] == 6:fraction_name = "Новостное Агенство"
            elif i['fraction'] == 7:fraction_name = "Казанская Банда"
            elif i['fraction'] == 8:fraction_name = "Окружная Больница"
            elif i['fraction'] == 9:fraction_name = "Чёрная Кошка"
            elif i['fraction'] == 10:fraction_name = "Санитары"
            elif i['fraction'] == 11:fraction_name = "Солнцевская братва"
            elif i['fraction'] == 12:fraction_name = "Русская Мафия"
            elif i['fraction'] == 13:fraction_name = "Украинская Мафия"
            elif i['fraction'] == 14:fraction_name = "Кавказкая Мафия"
            elif i['fraction'] == 15:fraction_name = "ФСБ"
            elif i['fraction'] == 16:fraction_name = "Армия"
            elif i['fraction'] == 17:fraction_name = "Тюрьма Строгого Режима"
            elif i['fraction'] == 40:fraction_name = "Генеральная Прокуратура"
            result += f"Ник: {i['nickname']}, Фракция: {fraction_name}, Преды/Выговоры: {i['preds']}/{i['vigs']}, Балов: {i['balls']}, Дней: {i['srok']}\n\n"
    else:
        print(f"Ошибка {data['message']}")
    bot.send_message(message.chat.id, result)
@bot.message_handler(func = lambda message: message.text == "Заместители[ЦО]")
def codep(message):
    bot.send_message(message.chat.id, "Ожидаем ответа API....")
    data = gx.get_deputies(server=201)
    bot.send_message(message.chat.id, "Формируем ответ....")
    if data["success"]:
        players = data['data']['players']
        result = ""
        for i in players:
            if i['fraction'] == 1:fraction_name = "Городская Полиция"
            elif i['fraction'] == 2:fraction_name = "Окружная полиция"
            elif i['fraction'] == 3:fraction_name = "Городская Больница"
            elif i['fraction'] == 4:fraction_name = "Правительство"
            elif i['fraction'] == 5:fraction_name = "Центр Лицензирования"
            elif i['fraction'] == 6:fraction_name = "Новостное Агенство"
            elif i['fraction'] == 7:fraction_name = "Казанская Банда"
            elif i['fraction'] == 8:fraction_name = "Окружная Больница"
            elif i['fraction'] == 9:fraction_name = "Чёрная Кошка"
            elif i['fraction'] == 10:fraction_name = "Санитары"
            elif i['fraction'] == 11:fraction_name = "Солнцевская братва"
            elif i['fraction'] == 12:fraction_name = "Русская Мафия"
            elif i['fraction'] == 13:fraction_name = "Украинская Мафия"
            elif i['fraction'] == 14:fraction_name = "Кавказкая Мафия"
            elif i['fraction'] == 15:fraction_name = "ФСБ"
            elif i['fraction'] == 16:fraction_name = "Армия"
            elif i['fraction'] == 17:fraction_name = "Тюрьма Строгого Режима"
            elif i['fraction'] == 40:fraction_name = "Генеральная Прокуратура"
            else:fraction_name = i['fraction']
            result += f"Ник: {i['nickname']} Фракция: {fraction_name}\n"
    else:
        print(f"Ошибка {data['message']}")
    bot.send_message(message.chat.id, result)

@bot.message_handler(func = lambda message: message.text == "Следящая администрация[ЮО]")
def uoadm(message):
    bot.send_message(message.chat.id, "В разработке...")
@bot.message_handler(func = lambda message: message.text == "Лидеры[ЮО]")
def uoled(message):
    bot.send_message(message.chat.id, "Ожидаем ответа API....")
    data = gx.get_leaders(server=202)
    bot.send_message(message.chat.id, "Формируем ответ....")
    if data["success"]:
        players = data['data']['players']
        result = ""
        for i in players:
            if i['fraction'] == 1:fraction_name = "Городская Полиция"
            elif i['fraction'] == 2:fraction_name = "Окружная полиция"
            elif i['fraction'] == 3:fraction_name = "Городская Больница"
            elif i['fraction'] == 4:fraction_name = "Правительство"
            elif i['fraction'] == 5:fraction_name = "Центр Лицензирования"
            elif i['fraction'] == 6:fraction_name = "Новостное Агенство"
            elif i['fraction'] == 7:fraction_name = "Казанская Банда"
            elif i['fraction'] == 8:fraction_name = "Окружная Больница"
            elif i['fraction'] == 9:fraction_name = "Чёрная Кошка"
            elif i['fraction'] == 10:fraction_name = "Санитары"
            elif i['fraction'] == 11:fraction_name = "Солнцевская братва"
            elif i['fraction'] == 12:fraction_name = "Русская Мафия"
            elif i['fraction'] == 13:fraction_name = "Украинская Мафия"
            elif i['fraction'] == 14:fraction_name = "Кавказкая Мафия"
            elif i['fraction'] == 15:fraction_name = "ФСБ"
            elif i['fraction'] == 16:fraction_name = "Армия"
            elif i['fraction'] == 17:fraction_name = "Тюрьма Строгого Режима"
            elif i['fraction'] == 40:fraction_name = "Генеральная Прокуратура"
            else:fraction_name = i['fraction']
            result += f"Ник: {i['nickname']}, Фракция: {fraction_name}, Преды/Выговоры: {i['preds']}/{i['vigs']}, Балов: {i['balls']}, Дней: {i['srok']}\n\n"
    else:
        print(f"Ошибка {data['message']}")
    bot.send_message(message.chat.id, result)
@bot.message_handler(func = lambda message: message.text == "Заместители[ЮО]")
def uodep(message):
    bot.send_message(message.chat.id, "Ожидаем ответа API....")
    data = gx.get_deputies(server=202)
    bot.send_message(message.chat.id, "Формируем ответ....")
    if data["success"]:
        players = data['data']['players']
        result = ""
        for i in players:
            if i['fraction'] == 1:fraction_name = "Городская Полиция"
            elif i['fraction'] == 2:fraction_name = "Окружная полиция"
            elif i['fraction'] == 3:fraction_name = "Городская Больница"
            elif i['fraction'] == 4:fraction_name = "Правительство"
            elif i['fraction'] == 5:fraction_name = "Центр Лицензирования"
            elif i['fraction'] == 6:fraction_name = "Новостное Агенство"
            elif i['fraction'] == 7:fraction_name = "Казанская Банда"
            elif i['fraction'] == 8:fraction_name = "Окружная Больница"
            elif i['fraction'] == 9:fraction_name = "Чёрная Кошка"
            elif i['fraction'] == 10:fraction_name = "Санитары"
            elif i['fraction'] == 11:fraction_name = "Солнцевская братва"
            elif i['fraction'] == 12:fraction_name = "Русская Мафия"
            elif i['fraction'] == 13:fraction_name = "Украинская Мафия"
            elif i['fraction'] == 14:fraction_name = "Кавказкая Мафия"
            elif i['fraction'] == 15:fraction_name = "ФСБ"
            elif i['fraction'] == 16:fraction_name = "Армия"
            elif i['fraction'] == 17:fraction_name = "Тюрьма Строгого Режима"
            elif i['fraction'] == 40:fraction_name = "Генеральная Прокуратура"
            else:fraction_name = i['fraction']
            result += f"Ник: {i['nickname']} Фракция: {fraction_name}\n"
    else:
        print(f"Ошибка {data['message']}")
    bot.send_message(message.chat.id, result)

@bot.message_handler(func = lambda message: message.text == "Следящая администрация[СО]")
def soadm(message):
    bot.send_message(message.chat.id, "В разработке...")
@bot.message_handler(func = lambda message: message.text == "Лидеры[СО]")
def soled(message):
    bot.send_message(message.chat.id, "Ожидаем ответа API....")
    data = gx.get_leaders(server=203)
    bot.send_message(message.chat.id, "Формируем ответ....")
    if data["success"]:
        players = data['data']['players']
        result = ""
        for i in players:
            if i['fraction'] == 1:fraction_name = "Городская Полиция"
            elif i['fraction'] == 2:fraction_name = "Окружная полиция"
            elif i['fraction'] == 3:fraction_name = "Городская Больница"
            elif i['fraction'] == 4:fraction_name = "Правительство"
            elif i['fraction'] == 5:fraction_name = "Центр Лицензирования"
            elif i['fraction'] == 6:fraction_name = "Новостное Агенство"
            elif i['fraction'] == 7:fraction_name = "Казанская Банда"
            elif i['fraction'] == 8: fraction_name = "Окружная Больница"
            elif i['fraction'] == 9: fraction_name = "Чёрная Кошка"
            elif i['fraction'] == 10:fraction_name = "Санитары"
            elif i['fraction'] == 11:fraction_name = "Солнцевская братва"
            elif i['fraction'] == 12:fraction_name = "Русская Мафия"
            elif i['fraction'] == 13:fraction_name = "Украинская Мафия"
            elif i['fraction'] == 14:fraction_name = "Кавказкая Мафия"
            elif i['fraction'] == 15:fraction_name = "ФСБ"
            elif i['fraction'] == 16:fraction_name = "Армия"
            elif i['fraction'] == 17:fraction_name = "Тюрьма Строгого Режима"
            elif i['fraction'] == 40:fraction_name = "Генеральная Прокуратура"
            else:fraction_name = i['fraction']
            result += f"Ник: {i['nickname']}, Фракция: {fraction_name}, Преды/Выговоры: {i['preds']}/{i['vigs']}, Балов: {i['balls']}, Дней: {i['srok']}\n\n"
    else:
        print(f"Ошибка {data['message']}")
    bot.send_message(message.chat.id, result)
@bot.message_handler(func = lambda message: message.text == "Заместители[СО]")
def sodep(message):
    bot.send_message(message.chat.id, "Ожидаем ответа API....")
    data = gx.get_deputies(server=203)
    bot.send_message(message.chat.id, "Формируем ответ....")
    if data["success"]:
        players = data['data']['players']
        result = ""
        for i in players:
            if i['fraction'] == 1:fraction_name = "Городская Полиция"
            elif i['fraction'] == 2:fraction_name = "Окружная полиция"
            elif i['fraction'] == 3:fraction_name = "Городская Больница"
            elif i['fraction'] == 4:fraction_name = "Правительство"
            elif i['fraction'] == 5:fraction_name = "Центр Лицензирования"
            elif i['fraction'] == 6:fraction_name = "Новостное Агенство"
            elif i['fraction'] == 7:fraction_name = "Казанская Банда"
            elif i['fraction'] == 8: fraction_name = "Окружная Больница"
            elif i['fraction'] == 9: fraction_name = "Чёрная Кошка"
            elif i['fraction'] == 10:fraction_name = "Санитары"
            elif i['fraction'] == 11:fraction_name = "Солнцевская братва"
            elif i['fraction'] == 12:fraction_name = "Русская Мафия"
            elif i['fraction'] == 13:fraction_name = "Украинская Мафия"
            elif i['fraction'] == 14:fraction_name = "Кавказкая Мафия"
            elif i['fraction'] == 15:fraction_name = "ФСБ"
            elif i['fraction'] == 16:fraction_name = "Армия"
            elif i['fraction'] == 17:fraction_name = "Тюрьма Строгого Режима"
            elif i['fraction'] == 40:fraction_name = "Генеральная Прокуратура"
            else:fraction_name = i['fraction']
            result += f"Ник: {i['nickname']} Фракция: {fraction_name}\n"
    else:
        print(f"Ошибка {data['message']}")
    bot.send_message(message.chat.id, result)

@bot.message_handler(func = lambda message: message.text == "Следящая администрация[ВО]")
def voadm(message):
    bot.send_message(message.chat.id, "В разработке...")
@bot.message_handler(func = lambda message: message.text == "Лидеры[ВО]")
def voled(message):
    bot.send_message(message.chat.id, "Ожидаем ответа API....")
    data = gx.get_leaders(server=204)
    bot.send_message(message.chat.id, "Формируем ответ....")
    if data["success"]:
        players = data['data']['players']
        result = ""
        for i in players:
            if i['fraction'] == 1:fraction_name = "Городская Полиция"
            elif i['fraction'] == 2:fraction_name = "Окружная полиция"
            elif i['fraction'] == 3:fraction_name = "Городская Больница"
            elif i['fraction'] == 4:fraction_name = "Правительство"
            elif i['fraction'] == 5:fraction_name = "Центр Лицензирования"
            elif i['fraction'] == 6:fraction_name = "Новостное Агенство"
            elif i['fraction'] == 7:fraction_name = "Казанская Банда"
            elif i['fraction'] == 8:fraction_name = "Окружная Больница"
            elif i['fraction'] == 9:fraction_name = "Чёрная Кошка"
            elif i['fraction'] == 10:fraction_name = "Санитары"
            elif i['fraction'] == 11:fraction_name = "Солнцевская братва"
            elif i['fraction'] == 12:fraction_name = "Русская Мафия"
            elif i['fraction'] == 13:fraction_name = "Украинская Мафия"
            elif i['fraction'] == 14:fraction_name = "Кавказкая Мафия"
            elif i['fraction'] == 15:fraction_name = "ФСБ"
            elif i['fraction'] == 16:fraction_name = "Армия"
            elif i['fraction'] == 17:fraction_name = "Тюрьма Строгого Режима"
            elif i['fraction'] == 40:fraction_name = "Генеральная Прокуратура"
            else:fraction_name = i['fraction']
            result += f"Ник: {i['nickname']}, Фракция: {fraction_name}, Преды/Выговоры: {i['preds']}/{i['vigs']}, Балов: {i['balls']}, Дней: {i['srok']}\n\n"
    else:
        print(f"Ошибка {data['message']}")
    bot.send_message(message.chat.id, result)
@bot.message_handler(func = lambda message: message.text == "Заместители[ВО]")
def vodep(message):
    bot.send_message(message.chat.id, "Ожидаем ответа API....")
    data = gx.get_deputies(server=204)
    bot.send_message(message.chat.id, "Формируем ответ....")
    if data["success"]:
        players = data['data']['players']
        result = ""
        for i in players:
            if i['fraction'] == 1:fraction_name = "Городская Полиция"
            elif i['fraction'] == 2:fraction_name = "Окружная полиция"
            elif i['fraction'] == 3:fraction_name = "Городская Больница"
            elif i['fraction'] == 4:fraction_name = "Правительство"
            elif i['fraction'] == 5:fraction_name = "Центр Лицензирования"
            elif i['fraction'] == 6:fraction_name = "Новостное Агенство"
            elif i['fraction'] == 7:fraction_name = "Казанская Банда"
            elif i['fraction'] == 8:fraction_name = "Окружная Больница"
            elif i['fraction'] == 9:fraction_name = "Чёрная Кошка"
            elif i['fraction'] == 10:fraction_name = "Санитары"
            elif i['fraction'] == 11:fraction_name = "Солнцевская братва"
            elif i['fraction'] == 12:fraction_name = "Русская Мафия"
            elif i['fraction'] == 13:fraction_name = "Украинская Мафия"
            elif i['fraction'] == 14:fraction_name = "Кавказкая Мафия"
            elif i['fraction'] == 15:fraction_name = "ФСБ"
            elif i['fraction'] == 16:fraction_name = "Армия"
            elif i['fraction'] == 17:fraction_name = "Тюрьма Строгого Режима"
            elif i['fraction'] == 40:fraction_name = "Генеральная Прокуратура"
            else:fraction_name = i['fraction']
            result += f"Ник: {i['nickname']} Фракция: {fraction_name}\n"
    else:
        print(f"Ошибка {data['message']}")
    bot.send_message(message.chat.id, result)


@bot.message_handler(func = lambda message: message.text == "Следящая администрация[ЗО]")
def zoadm(message):
    bot.send_message(message.chat.id, "В разработке...")
@bot.message_handler(func = lambda message: message.text == "Лидеры[ЗО]")
def zoled(message):
    bot.send_message(message.chat.id, "Ожидаем ответа API....")
    data = gx.get_leaders(server=205)
    bot.send_message(message.chat.id, "Формируем ответ....")
    if data["success"]:
        players = data['data']['players']
        result = ""
        for i in players:
            if i['fraction'] == 1:fraction_name = "Городская Полиция"
            elif i['fraction'] == 2:fraction_name = "Окружная полиция"
            elif i['fraction'] == 3:fraction_name = "Городская Больница"
            elif i['fraction'] == 4:fraction_name = "Правительство"
            elif i['fraction'] == 5:fraction_name = "Центр Лицензирования"
            elif i['fraction'] == 6:fraction_name = "Новостное Агенство"
            elif i['fraction'] == 7:fraction_name = "Казанская Банда"
            elif i['fraction'] == 8:fraction_name = "Окружная Больница"
            elif i['fraction'] == 9:fraction_name = "Чёрная Кошка"
            elif i['fraction'] == 10:fraction_name = "Санитары"
            elif i['fraction'] == 11:fraction_name = "Солнцевская братва"
            elif i['fraction'] == 12:fraction_name = "Русская Мафия"
            elif i['fraction'] == 13:fraction_name = "Украинская Мафия"
            elif i['fraction'] == 14:fraction_name = "Кавказкая Мафия"
            elif i['fraction'] == 15:fraction_name = "ФСБ"
            elif i['fraction'] == 16:fraction_name = "Армия"
            elif i['fraction'] == 17:fraction_name = "Тюрьма Строгого Режима"
            elif i['fraction'] == 40:fraction_name = "Генеральная Прокуратура"
            else:fraction_name = i['fraction']
            result += f"Ник: {i['nickname']}, Фракция: {fraction_name}, Преды/Выговоры: {i['preds']}/{i['vigs']}, Балов: {i['balls']}, Дней: {i['srok']}\n\n"
    else:
        print(f"Ошибка {data['message']}")
    bot.send_message(message.chat.id, result)
@bot.message_handler(func = lambda message: message.text == "Заместители[ЗО]")
def zodep(message):
    bot.send_message(message.chat.id, "Ожидаем ответа API....")
    data = gx.get_deputies(server=205)
    bot.send_message(message.chat.id, "Формируем ответ....")
    if data["success"]:
        players = data['data']['players']
        result = ""
        for i in players:
            if i['fraction'] == 1:fraction_name = "Городская Полиция"
            elif i['fraction'] == 2:fraction_name = "Окружная полиция"
            elif i['fraction'] == 3:fraction_name = "Городская Больница"
            elif i['fraction'] == 4:fraction_name = "Правительство"
            elif i['fraction'] == 5:fraction_name = "Центр Лицензирования"
            elif i['fraction'] == 6:fraction_name = "Новостное Агенство"
            elif i['fraction'] == 7:fraction_name = "Казанская Банда"
            elif i['fraction'] == 8:fraction_name = "Окружная Больница"
            elif i['fraction'] == 9:fraction_name = "Чёрная Кошка"
            elif i['fraction'] == 10:fraction_name = "Санитары"
            elif i['fraction'] == 11:fraction_name = "Солнцевская братва"
            elif i['fraction'] == 12:fraction_name = "Русская Мафия"
            elif i['fraction'] == 13:fraction_name = "Украинская Мафия"
            elif i['fraction'] == 14:fraction_name = "Кавказкая Мафия"
            elif i['fraction'] == 15:fraction_name = "ФСБ"
            elif i['fraction'] == 16:fraction_name = "Армия"
            elif i['fraction'] == 17:fraction_name = "Тюрьма Строгого Режима"
            elif i['fraction'] == 40:fraction_name = "Генеральная Прокуратура"
            else:fraction_name = i['fraction']
            result += f"Ник: {i['nickname']} Фракция: {fraction_name}\n"
    else:
        print(f"Ошибка {data['message']}")
    bot.send_message(message.chat.id, result)

@bot.message_handler(func = lambda message: message.text == "Следящая администрация[ПО]")
def poadm(message):
    bot.send_message(message.chat.id, "В разработке...")
@bot.message_handler(func = lambda message: message.text == "Лидеры[ПО]")
def poled(message):
    bot.send_message(message.chat.id, "Ожидаем ответа API....")
    data = gx.get_leaders(server=206)
    bot.send_message(message.chat.id, "Формируем ответ....")
    if data["success"]:
        players = data['data']['players']
        result = ""
        for i in players:
            if i['fraction'] == 1:fraction_name = "Городская Полиция"
            elif i['fraction'] == 2:fraction_name = "Окружная полиция"
            elif i['fraction'] == 3:fraction_name = "Городская Больница"
            elif i['fraction'] == 4:fraction_name = "Правительство"
            elif i['fraction'] == 5:fraction_name = "Центр Лицензирования"
            elif i['fraction'] == 6:fraction_name = "Новостное Агенство"
            elif i['fraction'] == 7:fraction_name = "Казанская Банда"
            elif i['fraction'] == 8:fraction_name = "Окружная Больница"
            elif i['fraction'] == 9:fraction_name = "Чёрная Кошка"
            elif i['fraction'] == 10:fraction_name = "Санитары"
            elif i['fraction'] == 11:fraction_name = "Солнцевская братва"
            elif i['fraction'] == 12:fraction_name = "Русская Мафия"
            elif i['fraction'] == 13:fraction_name = "Украинская Мафия"
            elif i['fraction'] == 14:fraction_name = "Кавказкая Мафия"
            elif i['fraction'] == 15:fraction_name = "ФСБ"
            elif i['fraction'] == 16:fraction_name = "Армия"
            elif i['fraction'] == 17:fraction_name = "Тюрьма Строгого Режима"
            elif i['fraction'] == 40:fraction_name = "Генеральная Прокуратура"
            else:fraction_name = i['fraction']
            result += f"Ник: {i['nickname']}, Фракция: {fraction_name}, Преды/Выговоры: {i['preds']}/{i['vigs']}, Балов: {i['balls']}, Дней: {i['srok']}\n\n"
    else:
        print(f"Ошибка {data['message']}")
    bot.send_message(message.chat.id, result)
@bot.message_handler(func = lambda message: message.text == "Заместители[ПО]")
def podep(message):
    bot.send_message(message.chat.id, "Ожидаем ответа API....")
    data = gx.get_deputies(server=206)
    bot.send_message(message.chat.id, "Формируем ответ....")
    if data["success"]:
        players = data['data']['players']
        result = ""
        for i in players:
            if i['fraction'] == 1:fraction_name = "Городская Полиция"
            elif i['fraction'] == 2:fraction_name = "Окружная полиция"
            elif i['fraction'] == 3:fraction_name = "Городская Больница"
            elif i['fraction'] == 4:fraction_name = "Правительство"
            elif i['fraction'] == 5:fraction_name = "Центр Лицензирования"
            elif i['fraction'] == 6:fraction_name = "Новостное Агенство"
            elif i['fraction'] == 7:fraction_name = "Казанская Банда"
            elif i['fraction'] == 8:fraction_name = "Окружная Больница"
            elif i['fraction'] == 9:fraction_name = "Чёрная Кошка"
            elif i['fraction'] == 10:fraction_name = "Санитары"
            elif i['fraction'] == 11:fraction_name = "Солнцевская братва"
            elif i['fraction'] == 12:fraction_name = "Русская Мафия"
            elif i['fraction'] == 13:fraction_name = "Украинская Мафия"
            elif i['fraction'] == 14:fraction_name = "Кавказкая Мафия"
            elif i['fraction'] == 15:fraction_name = "ФСБ"
            elif i['fraction'] == 16:fraction_name = "Армия"
            elif i['fraction'] == 17:fraction_name = "Тюрьма Строгого Режима"
            elif i['fraction'] == 40:fraction_name = "Генеральная Прокуратура"
            else:fraction_name = i['fraction']
            result += f"Ник: {i['nickname']} Фракция: {fraction_name}\n"
    else:
        print(f"Ошибка {data['message']}")
    bot.send_message(message.chat.id, result)

@bot.message_handler(func = lambda message: message.text == "Следящая администрация[ФО]")
def foadm(message):
    bot.send_message(message.chat.id, "В разработке...")
@bot.message_handler(func = lambda message: message.text == "Лидеры[ФО]")
def foled(message):
    bot.send_message(message.chat.id, "В разработке...")
@bot.message_handler(func = lambda message: message.text == "Заместители[ФО]")
def fodep(message):
    bot.send_message(message.chat.id, "В разработке...")

###################################################################################

@bot.message_handler(commands=['ping'])
def ping(message):
    bot.send_message(message.chat.id, "Я работаю!")

@bot.message_handler(commands=['time'])
def ping(message):
    bot.send_message(message.chat.id, vork_time)

@bot.message_handler(commands=['feedback'])
def feedback(message):
    result = ("#feedback \n" + "Text:" +message.text + "\n\nUserName:" + "@" +str(message.from_user.username) + "\nUserID:" +str(message.from_user.id))
    bot.send_message(-4132986047, result)

@bot.message_handler(commands=['pm'])
def pm(message):
    if message.from_user.id == ADMIN_IDS:
        msg = message.text
        to = msg.split()[1]
        message_text = msg.split()[2:]
        bot.send_message(to, message_text)
        loging = ("#pm \n" + "Text:" +message.text + "\n\nUserName:" + "@" +str(message.from_user.username) + "\nUserID:" +str(message.from_user.id))
        bot.send_message(-4132986047, loging)
    else: bot.send_message(message.chat.id,"Вы не являетесь разработчиком!😑")

@bot.message_handler(commands=['myid'])
def chatid(message):
    bot.send_message(message.chat.id, message.from_user.id) 

@bot.message_handler(commands=['chatid'])
def chatid(message):
    bot.send_message(message.chat.id, message.chat.id)

print("I am work")
bot.polling()