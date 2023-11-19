import datetime
import random



def read_from_file():
    f = open("demofile.txt", "r")
    message = f.read()
    print(message)
    return message

def get_greeting():
    g1_list = [
        'Good Evening ',
        'Happy Evening',
        'What\'s up?',
        'How\'s it going?'
    ]

    g2_list = [
        'Hope you are all having a great',
        'wishing you all a great',
    ]

    # get day of week
    x = datetime.datetime.now()
    day = x.strftime("%A")

    g1 = random.choice(g1_list)
    g2 = random.choice(g2_list)

    greeting = ' {} \n {} {}'.format(g1, g2, day)
    return greeting


def get_body():
    return 'I hav spent this evening debugging, its like being the detective in a crime drama where you are also the murderer'
def get_hashtags():
    return "#devs #100DaysOfCode"

def generate_message():
    message = ""
    greeting = get_greeting()
    body = get_body()
    hashtags = get_hashtags()
    message = " {} \n {} \n {}".format(greeting, body, hashtags)
    return message


