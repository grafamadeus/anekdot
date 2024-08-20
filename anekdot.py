import requests
from bs4 import BeautifulSoup as Bs
import telebot
from telebot import types
from config import TOKEN


def get_jokes():
    r = requests.get(url='https://www.anekdot.ru/')
    soup = Bs(r.text,'html.parser')
    items = soup.find_all('div',class_='text')
    
    for i in items:
        yield i.text


a = get_jokes()


bot = telebot.TeleBot(TOKEN)


menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu.row("Анекдот")



@bot.message_handler(commands=['start'])

def start(message):
    bot.send_message(message.chat.id,"Нажми на 'анекдот' и я отправлю анекдот", reply_markup=menu)



@bot.message_handler(func=lambda message:True)
def second(message):
    if message.text == "Анекдот":
        bot.send_message(message.chat.id,next(a))
    else:
        bot.send_message(message.chat.id, "Была одна задача. Нажимать на единственную кнопку и ты ее провалил(")
        return
        


bot.polling(non_stop=True)