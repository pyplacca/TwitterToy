from logging import INFO, ERROR
from utils import DB_PATH, DatabaseManager, TweetLogger
from auth import API
import asyncio


api = API
# user = api.me()

logger = TweetLogger()
# logger.log_message(msg='Tweeting - Test log 2')

tweet_db = DatabaseManager(DB_PATH)
# tweet_db.use_table('Tweets', timestamp='text', id='int', text='text', quote='int')

# print(api.get_settings())
