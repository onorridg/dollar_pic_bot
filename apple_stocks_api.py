import os

import requests

from dotenv import load_dotenv


load_dotenv()
ACCESS_KEY = str(os.getenv('ACCESS_KEY'))
MY_UUID = str(os.getenv('MY_UUID'))
USER_AGENT = str(os.getenv('USER_AGENT'))


def get_dollar():
    url = f'https://stocks-data-service.apple.com/api/v1/quote?language=en-GB&region=RU&symbol=RUB%3DX&dataSet=quote&accessKey={ACCESS_KEY}'
    headers = {
        'Host': 'stocks-data-service.apple.com',
        'X-Apple-Request-UUID': MY_UUID,
        'Accept': '*/*',
        'User-Agent': USER_AGENT,
        'Accept-Language': 'en-GB,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
    }

    response = requests.get(url=url, headers=headers).json()
    return response['quotes'][0]['quoteDetail']

#if __name__ == '__main__':
#    from pprint import pprint
#    pprint(get_dollar())