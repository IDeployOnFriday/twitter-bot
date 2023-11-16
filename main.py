import tweepy
import auth
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

if __name__ == '__main__':
    import tweepy

    client = tweepy.Client(consumer_key=auth.consumer_key,
                           consumer_secret=auth.consumer_secret,
                           access_token=auth.access_token,
                           access_token_secret=auth.access_token_secret)

    response = client.create_tweet(text='Devops ')

    print(response)

