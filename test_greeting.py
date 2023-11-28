import unittest

from greetings import get_greeting_time_of_day

class TestStringMethods(unittest.TestCase):
    def test_time_of_day(self):
        time_of_day = get_greeting_time_of_day(10)
        self.assertEqual(time_of_day, 'Morning')

        time_of_day = get_greeting_time_of_day(12)
        self.assertEqual(time_of_day, 'Afternoon')

        time_of_day = get_greeting_time_of_day(14)
        self.assertEqual(time_of_day, 'Afternoon')

        time_of_day = get_greeting_time_of_day(18)
        self.assertEqual(time_of_day, 'Evening')

        time_of_day = get_greeting_time_of_day(19)
        self.assertEqual(time_of_day, 'Evening')