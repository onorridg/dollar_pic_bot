# Dollar picture bot

UP          |  DOWN
:-------------------------:|:-------------------------:
|![stocks_rub](https://user-images.githubusercontent.com/83474704/159005664-0aab6a96-b175-45d0-816d-cd8d61a45616.png)|![stocks_rub_2](https://user-images.githubusercontent.com/83474704/159005672-5052eda3-3058-4459-9bb7-ea2d18179720.png)|
 
### Бот обновляет фото с курсом доллара в телеграм группе каждые 10 минут.
------

## Создайте .env в директории с `bot.py`:
```env
# TELEGRAM BOT API:
TG_BOT_TOKEN=  # токен телеграм бота
TG_ADMIN_ID=   # id админестратора телеграм группы
TG_GROUP_ID=   # id телеграм группы

# stocks-analytics-events.apple.com (reversed apple stocks api)
ACCESS_KEY=    # accessKey
MY_UUID=       # User-Agent
USER_AGENT=    # User-Agent

# Ваша UTC зона:
UTC_Z=
```

**ⓘ Для получения кредов для обращения к закрытому API stocks-analytics-events.apple.com используйте [mitmproxy](https://mitmproxy.org/) или [HTTP Catcher(IOS)](https://apps.apple.com/app/id1445874902)**
