import tweepy
from database import DatabaseManager, default_database
# from decouple import config
from os import environ as env
import time

print(env.get('TWITTER_API_KEY'))
# tweet_db.use_table('tweets', time='text', url='text', id='int')
# tweet_db = DatabaseManager(default_database)
# tweet_db.use_table('tweets')
# print(tweet_db.get(id='13bIigY3N'))
# tweet_db.insert(time=time.asctime(), url='https://twitter.com/0jfn208jns12noadoa90e', id='13bIigY3N')

