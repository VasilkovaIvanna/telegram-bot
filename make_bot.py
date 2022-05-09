import ast
import telebot
from telebot import types

from db import *
from utils import pretty_filter, pretty_advanced_filter

bot = telebot.TeleBot("5340722558:AAEox03sZQq39fIHqGSnW5gCk4eJX6hGO3M")


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Welcome, dear customer! \n"
                                      "Here you can choose make-up products! Our system will help you to match any type of item you want to.")
    start(message)


def start(message):
    keyboard = types.InlineKeyboardMarkup()
    keys = [types.InlineKeyboardButton(text='Find certain product', callback_data=str({'method': 'find_product'})),
            types.InlineKeyboardButton(text='Get matched products by descriptions', callback_data=str({'method': 'filter_product'}))]
    for key in keys:
        keyboard.add(key)
    bot.send_message(message.chat.id, text="To start with — select what kind of services do you prefer: ", reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def unknown(message):
    bot.send_message(message.chat.id, "Sorry, I didn't get you. Let I show you my two main options, mate.")
    start(message)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if ast.literal_eval(call.data)['method'] == "find_product":
        find_product(call)
    elif ast.literal_eval(call.data)['method'] == "filter_product":
        filter_product(call)
    elif ast.literal_eval(call.data)['method'] == 'find_by_price':
        set_price_filter(call)
    elif ast.literal_eval(call.data)['method'] == 'return_to_menu':
        start(call.message)
    elif ast.literal_eval(call.data)['method'] == "find_by_price_lips":
        bot.send_message(call.message.chat.id, pretty_filter(db_find_lips_by_range_price(ast.literal_eval(call.data)['range'][0], ast.literal_eval(call.data)['range'][1])))
    elif ast.literal_eval(call.data)['method'] == "find_by_price_eyes":
        bot.send_message(call.message.chat.id, pretty_filter(db_find_eyes_by_range_price(ast.literal_eval(call.data)['range'][0], ast.literal_eval(call.data)['range'][1])))
    elif ast.literal_eval(call.data)['method'] == "find_by_price_face":
        bot.send_message(call.message.chat.id, pretty_filter(db_find_face_by_range_price(ast.literal_eval(call.data)['range'][0], ast.literal_eval(call.data)['range'][1])))
    elif ast.literal_eval(call.data)['method'] == "find_by_price_lash":
        bot.send_message(call.message.chat.id, pretty_filter(db_find_lash_by_range_price(ast.literal_eval(call.data)['range'][0], ast.literal_eval(call.data)['range'][1])))
    elif ast.literal_eval(call.data)['method'] == "1_100_filter":
        find_by_price(call, (1, 100))
    elif ast.literal_eval(call.data)['method'] == "101_400_filter":
        find_by_price(call, (101, 400))
    elif ast.literal_eval(call.data)['method'] == "401_1000_filter":
        find_by_price(call, (401, 1000))
    elif ast.literal_eval(call.data)['method'] == "1001_2000_filter":
        find_by_price(call, (1001, 2000))
    elif ast.literal_eval(call.data)['method'] == "2000_plus_filter":
        find_by_price(call, (2001, 400000))

    elif ast.literal_eval(call.data)['method'] == "show_lips_products_types":
        show_lips_products_types(call)
    elif ast.literal_eval(call.data)['method'] == "show_eyes_products_types":
        show_eyes_products_types(call)
    elif ast.literal_eval(call.data)['method'] == "show_face_products_types":
        show_face_products_types(call)
    elif ast.literal_eval(call.data)['method'] == "show_lash_products_types":
        show_lash_products_types(call)
    elif ast.literal_eval(call.data)['method'] == "show_all_products_types":
        show_all_products_types(call)

    elif ast.literal_eval(call.data)['method'] == "show_lipglosses":
        bot.send_message(call.message.chat.id, pretty_advanced_filter(show_lipglosses()))
        return_to_menu(call)
    elif ast.literal_eval(call.data)['method'] == "show_lipliners":
        bot.send_message(call.message.chat.id, pretty_advanced_filter(show_lipliners()))
        return_to_menu(call)
    elif ast.literal_eval(call.data)['method'] == "show_lipsticks":
        bot.send_message(call.message.chat.id, pretty_advanced_filter(show_lipsticks()))
        return_to_menu(call)
    elif ast.literal_eval(call.data)['method'] == "show_liptints":
        bot.send_message(call.message.chat.id, pretty_advanced_filter(show_liptints()))
        return_to_menu(call)
    elif ast.literal_eval(call.data)['method'] == "show_all_lips_products":
        bot.send_message(call.message.chat.id, pretty_advanced_filter(show_all_lips_products()))
        return_to_menu(call)

    elif ast.literal_eval(call.data)['method'] == "show_eyeConcealers":
        bot.send_message(call.message.chat.id, pretty_advanced_filter(show_eyeConcealers()))
        return_to_menu(call)
    elif ast.literal_eval(call.data)['method'] == "show_eyeliners":
        bot.send_message(call.message.chat.id, pretty_advanced_filter(show_eyeliners()))
        return_to_menu(call)
    elif ast.literal_eval(call.data)['method'] == "show_eyeshadows":
        bot.send_message(call.message.chat.id, pretty_advanced_filter(show_eyeshadows()))
        return_to_menu(call)
    elif ast.literal_eval(call.data)['method'] == "show_mascara":
        bot.send_message(call.message.chat.id, pretty_advanced_filter(show_mascara()))
        return_to_menu(call)
    elif ast.literal_eval(call.data)['method'] == "show_all_eyes_products":
        bot.send_message(call.message.chat.id, pretty_advanced_filter(show_all_eyes_products()))
        return_to_menu(call)

    elif ast.literal_eval(call.data)['method'] == "show_BBcreams":
        bot.send_message(call.message.chat.id, pretty_advanced_filter(show_BBcreams()))
        return_to_menu(call)
    elif ast.literal_eval(call.data)['method'] == "show_blushes":
        bot.send_message(call.message.chat.id, pretty_advanced_filter(show_blushes()))
        return_to_menu(call)
    elif ast.literal_eval(call.data)['method'] == "show_bronzers":
        bot.send_message(call.message.chat.id, pretty_advanced_filter(show_bronzers()))
        return_to_menu(call)
    elif ast.literal_eval(call.data)['method'] == "show_mascara":
        bot.send_message(call.message.chat.id, pretty_advanced_filter(show_mascara()))
        return_to_menu(call)
    elif ast.literal_eval(call.data)['method'] == "show_face_primers":
        bot.send_message(call.message.chat.id, pretty_advanced_filter(show_face_primers()))
        return_to_menu(call)
    elif ast.literal_eval(call.data)['method'] == "show_concealers":
        bot.send_message(call.message.chat.id, pretty_advanced_filter(show_concealers()))
        return_to_menu(call)
    elif ast.literal_eval(call.data)['method'] == "show_all_face_products":
        bot.send_message(call.message.chat.id, pretty_advanced_filter(show_all_face_products()))
        return_to_menu(call)

    elif ast.literal_eval(call.data)['method'] == "show_brow_mascaras":
        bot.send_message(call.message.chat.id, pretty_advanced_filter(show_brow_mascaras()))
        return_to_menu(call)
    elif ast.literal_eval(call.data)['method'] == "show_brow_pencil":
        bot.send_message(call.message.chat.id, pretty_advanced_filter(show_brow_pencil()))
        return_to_menu(call)
    elif ast.literal_eval(call.data)['method'] == "show_brow_powders":
        bot.send_message(call.message.chat.id, pretty_advanced_filter(show_brow_powders()))
        return_to_menu(call)
    elif ast.literal_eval(call.data)['method'] == "show_lash_primers":
        bot.send_message(call.message.chat.id, pretty_advanced_filter(show_lash_primers()))
        return_to_menu(call)
    elif ast.literal_eval(call.data)['method'] == "show_all_lash_products":
        bot.send_message(call.message.chat.id, pretty_advanced_filter(show_all_lash_products()))
        return_to_menu(call)
    else:
        bot.send_message(call.message.chat.id, "Sorry, I didn't got you. Let I show you my two main options, mate.")
        start(call.message)


def find_product(call):
    keyboard = types.InlineKeyboardMarkup()
    keys = [types.InlineKeyboardButton(text='Find by price', callback_data=str({'method': 'find_by_price'})),
            types.InlineKeyboardButton(text='Return to previous menu', callback_data=str({'method': 'return_to_menu'}))]
    for key in keys:
        keyboard.add(key)
    bot.send_message(call.message.chat.id, text="Select options:", reply_markup=keyboard)


def set_price_filter(call):
    keyboard = types.InlineKeyboardMarkup()
    keys = [types.InlineKeyboardButton(text='1 -- 100', callback_data=str({'method': '1_100_filter'})),
            types.InlineKeyboardButton(text='101 -- 400', callback_data=str({'method': '101_400_filter'})),
            types.InlineKeyboardButton(text='401 -- 1000', callback_data=str({'method': '401_1000_filter'})),
            types.InlineKeyboardButton(text='1001 -- 2000', callback_data=str({'method': '1001_2000_filter'})),
            types.InlineKeyboardButton(text='2001+', callback_data=str({'method': '2000_plus_filter'})),
            types.InlineKeyboardButton(text='Back', callback_data=str({'method': 'return_to_menu'}))
            ]
    for key in keys:
        keyboard.add(key)
    bot.send_message(call.message.chat.id, text="Select range of price:", reply_markup=keyboard)


def find_by_price(call, range_filter):
    keyboard = types.InlineKeyboardMarkup()
    keys = [types.InlineKeyboardButton(text='Lips cosmetic', callback_data=str({'method': 'find_by_price_lips', 'range': range_filter})),
            types.InlineKeyboardButton(text='Eyes items', callback_data=str({'method': 'find_by_price_eyes', 'range': range_filter})),
            types.InlineKeyboardButton(text='Face tools', callback_data=str({'method': 'find_by_price_face', 'range': range_filter})),
            types.InlineKeyboardButton(text='Price lash', callback_data=str({'method': 'find_by_price_lash', 'range': range_filter})),
            types.InlineKeyboardButton(text='Back', callback_data=str({'method': 'return_to_menu'}))
            ]
    for key in keys:
        keyboard.add(key)
    bot.send_message(call.message.chat.id, text="Select what kind of products do you prefer find out by price?", reply_markup=keyboard)


def filter_product(call):
    keyboard = types.InlineKeyboardMarkup()
    keys = [types.InlineKeyboardButton(text='See lips cosmetic', callback_data=str({'method': 'show_lips_products_types'})),
            types.InlineKeyboardButton(text='See eyes items', callback_data=str({'method': 'show_eyes_products_types'})),
            types.InlineKeyboardButton(text='See face tools', callback_data=str({'method': 'show_face_products_types'})),
            types.InlineKeyboardButton(text='See lash stuff', callback_data=str({'method': 'show_lash_products_types'})),
            types.InlineKeyboardButton(text='See all', callback_data=str({'method': 'show_all_products_types'})),
            types.InlineKeyboardButton(text='Return to previous menu', callback_data=str({'method': 'return_to_menu'}))]
    for key in keys:
        keyboard.add(key)
    bot.send_message(call.message.chat.id, text="Select what kind of products do you prefer?", reply_markup=keyboard)


def show_lips_products_types(call):
    keyboard = types.InlineKeyboardMarkup()
    keys = [types.InlineKeyboardButton(text='See lip glosses', callback_data=str({'method': 'show_lipglosses'})),
            types.InlineKeyboardButton(text='See lip liners', callback_data=str({'method': 'show_lipliners'})),
            types.InlineKeyboardButton(text='See lipsticks', callback_data=str({'method': 'show_lipsticks'})),
            types.InlineKeyboardButton(text='See lip tints', callback_data=str({'method': 'show_liptints'})),
            types.InlineKeyboardButton(text='See all', callback_data=str({'method': 'show_all_lips_products'})),
            types.InlineKeyboardButton(text='Return to previous menu', callback_data=str({'method': 'return_to_menu'}))]
    for key in keys:
        keyboard.add(key)
    bot.send_message(call.message.chat.id, text="Select what kind of lips products do you prefer?", reply_markup=keyboard)


def show_eyes_products_types(call):
    keyboard = types.InlineKeyboardMarkup()
    keys = [types.InlineKeyboardButton(text='See eye concealers', callback_data=str({'method': 'show_eyeConcealers'})),
            types.InlineKeyboardButton(text='See eye liners', callback_data=str({'method': 'show_eyeliners'})),
            types.InlineKeyboardButton(text='See eye shadows', callback_data=str({'method': 'show_eyeshadows'})),
            types.InlineKeyboardButton(text='See eye mascara', callback_data=str({'method': 'show_mascara'})),
            types.InlineKeyboardButton(text='See all', callback_data=str({'method': 'show_all_eyes_products'})),
            types.InlineKeyboardButton(text='Return to previous menu', callback_data=str({'method': 'return_to_menu'}))]
    for key in keys:
        keyboard.add(key)
    bot.send_message(call.message.chat.id, text="Select what kind of eyes products do you prefer?", reply_markup=keyboard)


def show_face_products_types(call):
    keyboard = types.InlineKeyboardMarkup()
    keys = [types.InlineKeyboardButton(text='See BBcreams', callback_data=str({'method': 'show_BBcreams'})),
            types.InlineKeyboardButton(text='See blushes', callback_data=str({'method': 'show_blushes'})),
            types.InlineKeyboardButton(text='See bronzers', callback_data=str({'method': 'show_bronzers'})),
            types.InlineKeyboardButton(text='See face primers', callback_data=str({'method': 'show_face_primers'})),
            types.InlineKeyboardButton(text='See concealers', callback_data=str({'method': 'show_concealers'})),
            types.InlineKeyboardButton(text='See all', callback_data=str({'method': 'show_all_face_products'})),
            types.InlineKeyboardButton(text='Return to previous menu', callback_data=str({'method': 'return_to_menu'}))]
    for key in keys:
        keyboard.add(key)
    bot.send_message(call.message.chat.id, text="Select what kind of face products do you prefer?", reply_markup=keyboard)


def show_lash_products_types(call):
    keyboard = types.InlineKeyboardMarkup()
    keys = [types.InlineKeyboardButton(text='See brow mascaras', callback_data=str({'method': 'show_brow_mascaras'})),
            types.InlineKeyboardButton(text='See brow pencil', callback_data=str({'method': 'show_brow_pencil'})),
            types.InlineKeyboardButton(text='See brow powders', callback_data=str({'method': 'show_brow_powders'})),
            types.InlineKeyboardButton(text='See lash primers', callback_data=str({'method': 'show_lash_primers'})),
            types.InlineKeyboardButton(text='See all', callback_data=str({'method': 'show_all_lash_products'})),
            types.InlineKeyboardButton(text='Return to previous menu', callback_data=str({'method': 'return_to_menu'}))]
    for key in keys:
        keyboard.add(key)
    bot.send_message(call.message.chat.id, text="Select what kind of brows and lash products do you prefer?", reply_markup=keyboard)


def show_all_products_types(call):
    bot.send_message(call.message.chat.id, text=pretty_advanced_filter(show_all_products()))


def return_to_menu(call):
    keyboard = types.InlineKeyboardMarkup()
    keys = types.InlineKeyboardButton(text='Back', callback_data=str({'method': 'return_to_menu'}))
    keyboard.add(keys)
    bot.send_message(call.message.chat.id, text="Use button below to return to menu", reply_markup=keyboard)


def launch():
    bot.infinity_polling()
