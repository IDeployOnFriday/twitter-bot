import datetime
import post
from get_message import read_from_file


if __name__ == '__main__':
    print("starting up ")

    x = datetime.datetime.now()
    print(x.strftime("%A"))
    print(x.strftime("%H"))

    message = read_from_file()

    post.post_to_platform(message, False)

