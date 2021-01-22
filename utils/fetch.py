import asyncio
import requests


QUOTES_HOST_URL = 'https://pplrq.herokuapp.com/quotes/'
ROUTES = {
    '/': QUOTES_HOST_URL,
    '/authors': f'{QUOTES_HOST_URL}authors'
}


async def get_quote(id_=-1, retry=5, retry_delay=5.0):
    """
    :param id_: set to -1 means a random quote else id must be a positive number greater than 0
    :param retry: number of times to retry a request upon failure
    :param retry_delay: represents how long to wait (in seconds) before retrying
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
        res = requests.get(url)
        return res.json()
    except requests.exceptions.ConnectionError as error:
        if retry == 0:
            print('Max retry exceeded. Exiting...')
            raise error
        else:
            print(f'Failed to connect. Retrying..., retry={retry}')
            await asyncio.sleep(retry_delay)
            return await get_quote(id_, retry-1)
