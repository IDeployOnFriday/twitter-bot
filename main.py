import datetime
import sys

import post
from get_message import read_from_file, generate_message


if __name__ == '__main__':
    print("starting up ")

    if len(sys.argv) > 1:
        test_mode = sys.argv[1]
    else:
        test_mode = False
    print("in test mode :  {} ".format(test_mode))

    message = generate_message()

    post.post_to_platform(message, test_mode)

def get_post():

    x = datetime.datetime.now()
    # print(x.strftime("%A"))
    # print(x.strftime("%H"))

    message = generate_message()

    post.post_to_platform(message, False)


