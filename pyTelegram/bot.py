import random
import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.TOKEN)
welcome = True
phrases = ["Шляпокур","Курва дебильная","влажный цыган","ты часом на бутылке не катаешься", 
"Ты хавал борщ с пизды", "Вафледрон бородатый","писюнами обмазался и ходишь тупишь", "бомбищека","рванина",
"таскал вафлю","сёрбал мочу за гаражами","борозду зубами грыз","подзалупа","рвач"]

@bot.message_handler(content_types=['text'])
def lalalal(message):
    global welcome
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Generate")
    markup.add(item1)
    if welcome:
        bot.send_message(message.chat.id, "Говорят ты петушара",reply_markup=markup)
        welcome = False
    else:
        if message.text == "Generate":
            bot.send_message(message.chat.id, random.choice(phrases),reply_markup=markup)

bot.polling(none_stop=True)