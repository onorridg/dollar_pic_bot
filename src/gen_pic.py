import os
from datetime import datetime, timedelta

from PIL import Image, ImageDraw, ImageFont

from dotenv import load_dotenv


load_dotenv()
UTC_Z = int(os.getenv('UTC_Z'))


def get_img(price, open_price, low_price, high_price):
    W = 1024
    price = round(price, 2)
    open_price = round(open_price, 2)
    low_price = round(low_price, 2)
    high_price = round(high_price, 2)
    percent = round(((price * 100 / open_price) - 100), 2)
    info = f'Open: {open_price}  Low: {low_price}  High: {high_price}'

    now = datetime.now() + timedelta(hours=UTC_Z)
    last_upd = str(now.strftime('%H:%M:%S %d.%m.%y'))

    red_percent= (255, 0, 0)
    green_percent = (64, 229, 70)

    if percent >= 0: 
        img = Image.new('RGB', (1024, 1024), color=green_percent)
    else:
        img = Image.new('RGB', (1024, 1024), color=red_percent)

    d = ImageDraw.Draw(img)
    
    font_price = ImageFont.truetype("ttf/Roboto-Bold.ttf", 270)
    font_percent = ImageFont.truetype("ttf/RobotoCondensed-Regular.ttf", 150)
    font_info = ImageFont.truetype("ttf/RobotoCondensed-Regular.ttf", 54)

    w_price= d.textlength(str(price), font=font_price)
    w_percent = d.textlength(' ' + str(percent) + ' %', font=font_percent)
    w_info = d.textlength(info, font=font_info)
    w_last_upd = d.textlength(str(last_upd), font=font_info)


    d.text(((W - w_price) / 2, 200), str(price), fill=(255,255,255), font=font_price)
    if percent >= 0:
        d.text(((W - w_percent) / 2, 460), '+' + str(percent) + ' %', fill=red_percent, font=font_percent)
    else:
        d.text(((W - w_percent) / 2, 460), str(percent) + ' %', fill=green_percent, font=font_percent)
    d.text(((W - w_info) / 2, 660), info, fill=(255, 255, 255), font=font_info)
    d.text(((W - w_last_upd) / 2, 800), last_upd, fill=(0, 0, 0), font=font_info)    


    img.save('stocks_rub.png')



if __name__ == '__main__':
    get_img(103.61, 102.38, 100.62, 104.18)
    get_img(90.61, 102.38, 100.62, 104.18)

