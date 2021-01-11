from .fetch import get_quote
from .logger import TweetLogger


class QueryRow(dict):
    def __init__(self, keys, values):
        arg_zip = zip(keys, values)
        super().__init__(dict(arg_zip))
        for key, value in arg_zip:
            try:
                getattr(self, key)
                key = f'{key}_'
            except AttributeError:
                pass
            setattr(self, key, value)
