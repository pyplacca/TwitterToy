import logging

import requests
import asyncio
import json
import time
from logging import INFO, ERROR, getLevelName

from tweepy.error import TweepError

import __config__ as conf
from auth import API
from utils import DatabaseManager, TweetLogger, get_quote, convert_time, truncate


# =====================================
# Global Variables and Class Instances
# =====================================
api = API

logger = TweetLogger()

database = DatabaseManager(conf.DB_PATH)
database.use_table('Tweets', timestamp='text', id='int', quote='int')


# ===================
# Main task
# ===================
async def main():
    number_of_tweets = 6
    restart_delay = 10.0
    quote_id = -1

    while True:
        restart = next_tweet = False
        log_msg = ''
        logger.setLevel(ERROR)

        try:
            quote = await get_quote(quote_id, 3)  # fetches quote to tweet

            if not database.get(quote=quote['id']):
                quote_id = quote['id']

                try:
                    # tweet received quote
                    tweet = api.update_status(status=f"{quote['quote']}\n\n- {quote['author']}")

                    if tweet.id:
                        print(f'Tweet posted: {tweet.id} -> {truncate(tweet.text, 57)!r}')
                        # record tweet in the database
                        database.insert(timestamp=time.asctime(), id=tweet.id, quote=quote['id'])
                        logger.setLevel(INFO)
                        log_msg = f'Tweet {tweet.id_str} successful'
                        quote_id = -1
                        next_tweet = True

                    else:
                        log_msg = f"Tweet failed - quote:{quote['id']}"

                except TweepError as tweet_error:
                    tweet_error = json.loads(tweet_error.response.text)['errors'].pop()
                    print(tweet_error)
                    log_msg = f"Tweet failed - {tweet_error['code']} - {tweet_error['message']}"

            else:
                log_msg = f"Quote {quote['id']} already tweeted"

        except requests.exceptions.ConnectionError as conn_error:
            log_msg = 'Connection error -> Failed to fetch quote'
            restart = True

        finally:
            print(f"Logging message: {log_msg}")
            await logger.log_message(msg=log_msg)

            if next_tweet:
                snooze_time = (24 / number_of_tweets) * 60 * 60
                print(f"Snoozing for {convert_time(snooze_time)} until next tweet 💤")
                await asyncio.sleep(snooze_time)

            if restart:
                print('\nRestarting...')
                await asyncio.sleep(restart_delay)


async def test_main():
    while True:
        await asyncio.sleep(2)
        print('What is this async await thingy?')


async def test_main_2():
    while True:
        await asyncio.sleep(1.35)
        print('Running some random async task...')


# =====================================
# Task Runner
# =====================================
async def async_tasks():
    return await asyncio.gather(
        main(),
        # test_main(),
        # test_main_2()
    )

if __name__ == '__main__':
    print('Firing up the bot\'s engine...')
    asyncio.run(async_tasks())
