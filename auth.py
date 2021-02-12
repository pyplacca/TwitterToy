from os import environ as env
import tweepy


API_KEY = env.get('TWITTER_API_KEY')
API_SECRET_KEY = env.get('TWITTER_API_SECRET_KEY')
ACCESS_TOKEN = env.get('TWITTER_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = env.get('TWITTER_ACCESS_TOKEN_SECRET')


class TweetAPIHandler:
    # authenticate user
    def __init__(self):
        self.auth = tweepy.OAuthHandler(
            API_KEY,
            API_SECRET_KEY
        )
        self.auth.set_access_token(
            ACCESS_TOKEN,
            ACCESS_TOKEN_SECRET
        )

    @property
    def api(self):
        # configure api
        return tweepy.API(self.auth, retry_count=3, retry_delay=10)


API = TweetAPIHandler().api
