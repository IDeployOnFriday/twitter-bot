import datetime
import secrets
from greetings import get_greeting
from hashtags import get_hashtags

def generate_message():
    greeting = get_greeting()
    num_of_days_update = get_100_days_code()
    hashtags = get_hashtags()
    message = "{} \n {} \n {}".format(greeting, num_of_days_update, hashtags)
    return message

def get_100_days_message() -> str:
    tag_list = [
        '#100DaysOfCode',
        '100 days of code',
        '#100DaysChallenge',
        '100 Days Challenge'
    ]

    return secrets.choice(tag_list)

def get_ending() -> str:
    tag_list = [
        'Completed',
        'Finished',
        'Done',
    ]

    return secrets.choice(tag_list)


def get_100_days_code() -> str:
    today = datetime.datetime.now()

    d0 = datetime.date(2023, 10, 8)
    d1 = datetime.date(today.year, today.month, today.day)
    delta = d1 - d0

    message = "✅ Day {}/100 of the {} {}! {} {}".format(str(delta.days),
                                                         get_100_days_message(),
                                                         get_ending(),
                                                         get_random_emoji(),
                                                         get_random_emoji())

    return message

def get_random_emoji() -> str:
    h1_list = [
        '✨',
        '🚀',
        '🎉',
        '💪💡',
        '📚'
    ]
    return secrets.choice(h1_list)
    
    
