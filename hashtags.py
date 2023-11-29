import random
def get_hashtags() -> str:
    h1_list = [
        '#devs',
        '#CodingJourney',
        '#100DaysChallenge',
        '#LearnToCode',
        '#Coding',
        '#DevOps',
        '#technology'
    ]

    hashtag2 = random.choice(h1_list)
    hashtags = '{} {} '.format("#100DaysOfCode", hashtag2)

    return hashtags
