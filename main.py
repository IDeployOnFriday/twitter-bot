import datetime
import post
from get_message import read_from_file, generate_message


if __name__ == '__main__':
    print("starting up ")

    message = generate_message()

    post.post_to_platform(message, True)

def get_post():

    x = datetime.datetime.now()
    # print(x.strftime("%A"))
    # print(x.strftime("%H"))

    message = generate_message()

    post.post_to_platform(message, False)


