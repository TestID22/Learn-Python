import random
import telebot
import config
from telebot import types


bot = telebot.TeleBot(config.TOKEN)
hp = 100
welcome = True
phrases = ["Шляпокур", "чепуховец проткнутый", "Ты чё, вафлица писюнами обмазался и ходишь тупишь",
           "Ты случайно на бутылке не катаешься?", "Вафледрон бородатый", "Ввалил тебе защеку", "Ты борщ с пизды отхавал",
           "Рваный туз", "Журила подхуйный", "Подзалупа", "Пригуби хуйца"
           ]


@bot.message_handler(content_types=["text"])
def lalala(msg):
    global welcome
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item2 = types.KeyboardButton("Отхуесосить Васю")
    markup.add(item2)
    if welcome:
        sticker = open("static/николя.jpg", "rb")
        bot.send_photo(msg.chat.id, sticker)
        bot.send_message(msg.chat.id, f"Здоров хуйло, eбать!Говорят {msg.from_user.first_name} работал щеками", reply_markup=markup)
        welcome = False
    else:
        if msg.text == "Отхуесосить Васю":
            sticker = open("static/николя — копия.jpg", "rb")
            bot.send_photo(msg.chat.id, sticker)
            bot.send_message(msg.chat.id, "Вася - " + random.choice(phrases), reply_markup=markup)

if __name__ == '__main__':
    bot.polling(none_stop=True)
