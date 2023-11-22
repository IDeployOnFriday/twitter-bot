import datetime
import random


def read_from_file():
    f = open("demofile.txt", "r")
    message = f.read()
    print(message)
    return message


def read_list_from_file():
    with open('demofile.txt') as f:
        lines = f.read().splitlines()
    print(lines)

    g1 = random.choice(lines)
    print(g1)
    return lines


def get_greeting():
    comunity_list = [
        'software engineers',
        'Coders',
        'Devs',
        'Developers',
        'Developers and HTML\'ers',
        'Python\'ers',
        'The Java crew'
    ]

    g1_list = [
        'Good {}',
        'What\'s up?',
        'How\'s it going?'
    ]

    # get day of week
    day = datetime.datetime.now().strftime("%A")

    time_of_day = get_greeting_time_of_day(int(datetime.datetime.now().strftime("%H")))

    g1 = random.choice(g1_list).format(time_of_day)
    comunity = random.choice(comunity_list)

    greeting = ' {}, {} '.format(g1, comunity)
    return greeting


def get_greeting_time_of_day(hour):
    if hour < 12:
        time_of_day = 'Morning'
    elif 12 < hour < 18:
        time_of_day = 'Afternoon'
    elif hour > 18:
        time_of_day = 'Evening'
    return time_of_day


def get_body():
    # open the sample file used
    file = open('update.txt')

    # read the content of the file opened
    content = file.readlines()

    file.close()

    today = datetime.datetime.now()
    d0 = datetime.date(2023, 11, 22)
    d1 = datetime.date(today.year, today.month, today.day)
    delta = d1 - d0

    line = content[delta.days]

    return (line)


def get_hashtags():
    return "#devs #100DaysOfCode"


def generate_message():
    greeting = get_greeting()
    num_of_days_update = get_100_days_code()
    body = get_body()
    hashtags = get_hashtags()
    message = "{} \n {} \n {} \n {}".format(greeting, num_of_days_update, body, hashtags)
    return message


def get_100_days_code():

    learning_list = [
        ', Today i am learning',
        ', Today i am revisiting',
        ', Today i hope to understand better'
    ]
    today = datetime.datetime.now()

    d0 = datetime.date(2023, 10, 8)
    d1 = datetime.date(today.year, today.month, today.day)
    delta = d1 - d0
    message_end = g1 = random.choice(learning_list)
    message = "100 Days of code, Day " + str(delta.days) + message_end
    return message
