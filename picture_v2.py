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
    procent = round(((price * 100 / open_price) - 100), 2)
    info = f'Open: {open_price}  Low: {low_price}  High: {high_price}'

    now = datetime.now() + timedelta(hours=UTC_Z)
    last_upd = str(now.strftime('%H:%M:%S %d.%m.%y'))

    red_procent = (255, 0, 0)
    green_procent = (64, 229, 70)

    if procent >= 0: 
        img = Image.new('RGB', (1024, 1024), color=green_procent)
    else:
        img = Image.new('RGB', (1024, 1024), color=red_procent)

    d = ImageDraw.Draw(img)
    
    font_price = ImageFont.truetype("ttf/Roboto-Bold.ttf", 270)
    font_procent = ImageFont.truetype("ttf/RobotoCondensed-Regular.ttf", 150)
    font_info = ImageFont.truetype("ttf/RobotoCondensed-Regular.ttf", 54)

    w_price, _ = d.textsize(str(price), font=font_price)
    w_procent, _ = d.textsize(' ' + str(procent) + ' %', font=font_procent)
    w_info, _ = d.textsize(info, font=font_info)
    w_last_upd, _ = d.textsize(str(last_upd), font=font_info)


    d.text(((W - w_price) / 2, 200), str(price), fill=(255,255,255), font=font_price)
    if procent >= 0:
        d.text(((W - w_procent) / 2, 460), '+' + str(procent) + ' %', fill=red_procent, font=font_procent)
    else:
        d.text(((W - w_procent) / 2, 460), str(procent) + ' %', fill=green_procent, font=font_procent)
    d.text(((W - w_info) / 2, 660), info, fill=(255, 255, 255), font=font_info)
    d.text(((W - w_last_upd) / 2, 800), last_upd, fill=(0, 0, 0), font=font_info)    


    img.save('stocks_rub.png')



if __name__ == '__main__':
    #get_img(103.61, 102.38, 100.62, 104.18)
    get_img(90.61, 102.38, 100.62, 104.18)

