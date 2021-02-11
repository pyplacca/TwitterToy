from __version__ import __title__
from __config__ import ROOT_DIR
import logging
import time
import os


LOG_FILE = os.path.join(ROOT_DIR, 'tweets.log')

LOG_HANDLER = logging.FileHandler(LOG_FILE, encoding='utf-8')

DEFAULT_LEVEL = logging.INFO


class TweetLogger(logging.Logger):
    def __init__(self):
        super().__init__(f'{__title__}.TweetLogger', DEFAULT_LEVEL)
        self.addHandler(LOG_HANDLER)
        self.setLevel(logging.getLevelName(DEFAULT_LEVEL))

    async def log_message(self, level: int = None, msg: str = '') -> None:
        log_level = level or self.getEffectiveLevel()
        message = logging.BASIC_FORMAT % ({
            'levelname': logging.getLevelName(log_level),
            'message': msg,
            'name': self.name
        })
        self.log(
            log_level,
            f"{time.strftime('%a %b %d %Y %H:%M:%S')} - {message}"
        )
