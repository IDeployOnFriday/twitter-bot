import datetime
import random
def get_greeting()  -> str:
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

def get_greeting_time_of_day(hour) -> str:
    time_of_day = 'Morning'

    if 12 <= hour < 18:
        time_of_day = 'Afternoon'
    elif hour >= 18:
        time_of_day = 'Evening'
    return time_of_day