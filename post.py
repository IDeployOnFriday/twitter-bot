import tweepy
import auth
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)


def post_to_platform(message, test):
    if test:
        client = tweepy.Client(consumer_key=auth.consumer_key,
                               consumer_secret=auth.consumer_secret,
                               access_token=auth.access_token,
                               access_token_secret=auth.access_token_secret)

        response = client.create_tweet(text=message)
    else:
        print(".......... \n" + message)
