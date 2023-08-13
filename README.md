# Dollar picture bot

|                                                          UP                                                          |                                                          DOWN                                                          |
| :------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------: |
| ![stocks_rub](https://user-images.githubusercontent.com/83474704/159005664-0aab6a96-b175-45d0-816d-cd8d61a45616.png) | ![stocks_rub_2](https://user-images.githubusercontent.com/83474704/159005672-5052eda3-3058-4459-9bb7-ea2d18179720.png) |
 
### Бот обновляет фото с курсом доллара в телеграм группе каждые 10 минут.
------

## Создайте .env в директории с `bot.py`:
```env
# TELEGRAM BOT API:
TG_BOT_TOKEN=  # токен телеграм бота
TG_ADMIN_ID=   # id администратора телеграм группы
TG_GROUP_ID=   # id телеграм группы

# stocks-analytics-events.apple.com (reversed apple stocks api)
ACCESS_KEY=    # accessKey
MY_UUID=       # User-Agent
USER_AGENT=    # User-Agent

# Ваша UTC зона:
UTC_Z=
```

**ⓘ Для получения кредов для обращения к закрытому API stocks-analytics-events.apple.com используйте [mitmproxy](https://mitmproxy.org/) или [HTTP Catcher(IOS)](https://apps.apple.com/app/id1445874902)**

---
## Получение id пользователя и группы:
* Создайте бота через [@BotFather](https://t.me/BotFather)
* Добавьте бота в нужную группу
* Сделайте запрос (можно прям через строку браузера). Нужно заменить `<YourBOTToken>` на токен, который вам выдал [@BotFather](https://t.me/BotFather)
```http
https://api.telegram.org/bot<YourBOTToken>/getUpdates
```
Ответ будет в виде `JSON`. 
* Ищем `my_chat_member:from:id:1234567890`. Копируем `id` и добавляем в `.env` для поля `TG_ADMIN_ID`.
* Ищем `my_chat_member:chat:id:-1234567890`. Копируем `id` и добавляем в `.env` для поля `TG_GROUP_ID`.

## Выдаем права боту:
После добавления бота в группу, добавляем его в администраторы и выдаем следующие права:
* Изменение профиля группы (для изменения фото группы на фото курса)
* Удаление сообщений (удаление сообщений об изменении фото, и для удаления самого обновленного фото из сообщений. Всё это нужно, чтобы не засорять группу.)

## Как это выглядит со тороны:
<img src="https://github.com/onorridg/dollar_pic_bot/assets/83474704/c2de22ab-7582-4093-aad3-d99bac2ab33b" width="30%" height="30%"></br>
<img src="https://github.com/onorridg/dollar_pic_bot/assets/83474704/f980ccb9-b4ca-487a-8f52-3fe0755802cf" width="30%" height="30%">
