import os
import time

from apple_stocks_api import get_dollar
from gen_pic import get_img

import telebot

from dotenv import load_dotenv


load_dotenv()
TELEGRAM_TOKEN = str(os.getenv('TG_BOT_TOKEN'))
TG_ADMIN_ID = int(os.getenv('TG_ADMIN_ID'))
TG_GROUP_ID = int(os.getenv('TG_GROUP_ID'))
IMG_NAME = 'stocks_rub.png'

bot = telebot.TeleBot(TELEGRAM_TOKEN)


def set_photo(flag=0):
    photo = open(IMG_NAME, 'rb')
    bot.set_chat_photo(TG_GROUP_ID, photo)
    message = bot.send_message(TG_GROUP_ID, '.')
    bot.delete_message(TG_GROUP_ID, message.id)
    bot.delete_message(TG_GROUP_ID, message.id - 1)
    photo.close()

def get_result():
    data = get_dollar()
    get_img(
        data['price'],
        data['dayOpenPrice'],
        data['dayLowPrice'], 
        data['dayHighPrice']
        )


bot.send_message(TG_ADMIN_ID, f'[+] Bot started')
try:
    while True:
        get_result()
        set_photo()
        time.sleep(600)
except Exception as err:
    bot.send_message(TG_ADMIN_ID, f'[!] Bot offline !\n\n{err}')