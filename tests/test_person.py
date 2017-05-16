import unittest
from classes.person import Person


class PersonClassTest(unittest.TestCase):
    my_class_instance = Person("staff", "Peter", "Musonye", "Y")

    def test_full_name_returns_actual_full_name(self):
        full_name = self.my_class_instance.full_name()
        self.assertEqual(full_name, 'Peter Musonye')
