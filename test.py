from get_message import  get_100_days_code, get_random_emoji
from main import get_post
import unittest

class TestStringMethods(unittest.TestCase):

    def test_post(self):
        message = get_post()

    def test_multi(self):
        i = 1
        while i < 10:
            message = self.test_post()
            i += 1

        print("Everything passed")

    def test_get_100_days_code(self):
        message = get_100_days_code()
        print(message)

    def test_get_random_emoji(self):
        emoji = get_random_emoji()
        print(emoji)

if __name__ == '__main__':
    unittest.main()