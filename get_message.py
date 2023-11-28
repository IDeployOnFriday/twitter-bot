import datetime
from greetings import get_greeting
from hashtags import get_hashtags

def generate_message():
    greeting = get_greeting()
    num_of_days_update = get_100_days_code()
    hashtags = get_hashtags()
    message = "{} \n {} \n {}".format(greeting, num_of_days_update, hashtags)
    return message


def get_100_days_code() -> str:
    today = datetime.datetime.now()

    d0 = datetime.date(2023, 10, 8)
    d1 = datetime.date(today.year, today.month, today.day)
    delta = d1 - d0
    message = "100 Days of code, Day " + str(delta.days)
    return message
