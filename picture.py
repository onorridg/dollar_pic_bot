import os
from datetime import datetime, timedelta

from PIL import Image, ImageDraw, ImageFont

from dotenv import load_dotenv


load_dotenv()
UTC_Z = int(os.getenv('UTC_Z'))


def get_img(price, open_price, low_price, high_price):
    price = round(price, 2)
    open_price = round(open_price, 2)
    low_price = round(low_price, 2)
    high_price = round(high_price, 2)
    procent = round(((price * 100 / open_price) - 100), 2)

    now = datetime.now() + timedelta(hours=UTC_Z)
    last_upd = str(now.strftime('%H:%M:%S %d.%m.%y'))

    red_procent = (230, 75, 60)
    green_procent = (0, 203, 95)

    img = Image.new('RGB', (1024, 1024), color=(34, 33, 35))
    d = ImageDraw.Draw(img)

    font_rubx = ImageFont.truetype("Roboto-Bold.ttf", 140)
    font_usdrub = ImageFont.truetype("Roboto-Bold.ttf", 80)
    font_dollar = ImageFont.truetype("Roboto-Bold.ttf", 80)
    font_procent = ImageFont.truetype("RobotoCondensed-Regular.ttf", 80)
    font_more = ImageFont.truetype("RobotoCondensed-Regular.ttf", 50)


    d.text((85, 290), 'RUB=₽', fill=(255,255,255), font=font_rubx)
    d.text((590, 345), 'USD/RUB', fill=(139, 138, 141), font=font_usdrub)
    d.line((60, 480, 954, 480), fill=(62, 62, 64), width=3)
    d.text((250, 530), str(price), fill=(255,255,255), font=font_dollar)
    if procent >= 0:
        d.text((520, 520), '+' + str(procent) + ' %', fill=green_procent, font=font_procent)
    else:
        d.text((520, 520), str(procent) + ' %', fill=red_procent, font=font_procent)
    d.text((105, 650), 'Open: ' + str(open_price), fill=(139, 138, 141), font=font_more)
    d.text((405, 650), 'Low: ' + str(low_price), fill=(139, 138, 141), font=font_more)
    d.text((685, 650), 'High: ' + str(high_price), fill=(139, 138, 141), font=font_more)
    if procent >= 0: 
        d.ellipse((0, 0, 1024, 1024), outline=green_procent, width=33)
    else:
        d.ellipse((0, 0, 1024, 1024), outline=red_procent, width=33)

    d.text((300, 760), f'UPD: {last_upd}', fill=(255, 87, 34), font=font_more)

    img.save('stocks_rub.png')
