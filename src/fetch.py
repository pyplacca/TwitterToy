import requests
import asyncio
import json


HEADERS = {'User-Agent': 'Chrome'}
QUOTES_HOST_URL = 'https://pplrq.herokuapp.com/quotes/'
ROUTES = {
    '/': QUOTES_HOST_URL,
    '/authors': f'{QUOTES_HOST_URL}authors'
}


async def get_quote(id_=-1, retry=5):
    """
    :param id_: set to -1 means a random quote else id must be a positive number greater than 0
    :param retry: number of times to retry a request upon failure
    :return: a dict object of a random quote or one with a specified id from the quotes api
    """
    if id_ != -1:
        if id_ < 1:
            raise ValueError('id must be -1 or a positive number greater than 0')
        else:
            param = id_
    else:
        param = ''
    try:
        url = f"{ROUTES['/']}{param}"
        res = requests.request('GET', url, headers=HEADERS)
        return json.loads(res.json())
    except ConnectionError as error:
        if retry == 0:
            return error
        else:
            print(f'Retrying..., retry={retry}')
            await asyncio.sleep(5.0)
            return get_quote(id_, retry-1)
