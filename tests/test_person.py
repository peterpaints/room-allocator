import unittest
from classes.person import Person


class PersonClassTest(unittest.TestCase):
    def test_full_name_only_returns_strings(self):
        with self.assertRaises(ValueError, msg='Only strings are allowed as names'):
            my_class_instance = Person("staff", "Peter", "Musonye")
            my_class_instance.full_name()
