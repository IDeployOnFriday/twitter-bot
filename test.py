from get_message import get_greeting_time_of_day, read_list_from_file, get_100_days_code
from main import get_post
import unittest

class TestStringMethods(unittest.TestCase):

    def test_post(self):
        message = get_post()

    def test_read_from_file(self):
        message = read_list_from_file()





    def test_multi(self):
        i = 1
        while i < 10:
            message = self.test_post()
            i += 1

        print("Everything passed")

    def test_get_100_days_code(self):
        get_100_days_code()

if __name__ == '__main__':
    unittest.main()