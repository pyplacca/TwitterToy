from __version__ import __title__
import logging
import time
import os


LOG_FILE = os.path.join(
    os.environ.get('USERPROFILE'),
    f'.{__title__}',
    'tweets.log'
)

try:
    open(LOG_FILE)
except FileNotFoundError:
    try:
        os.mkdir(os.path.dirname(LOG_FILE))
    except FileExistsError:
        pass

LOG_HANDLER = logging.FileHandler(LOG_FILE, encoding='utf-8')

DEFAULT_LEVEL = logging.INFO


class TweetLogger(logging.Logger):
    def __init__(self):
        super().__init__(f'{__title__}.TweetLogger', DEFAULT_LEVEL)
        self.addHandler(LOG_HANDLER)

    def log_message(self, level: int = DEFAULT_LEVEL, msg: str = '') -> None:
        log_level = level
        message = logging.BASIC_FORMAT % ({
            'levelname': logging.getLevelName(log_level),
            'message': msg,
            'name': self.name
        })
        self.log(
            log_level,
            f"{time.strftime('%a %b %d %Y %H:%M:%S')} - {message}"
        )
