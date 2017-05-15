import unittest
from classes.room import Room


class RoomClassTest(unittest.TestCase):
    pass
    # def test_create_room_successfully(self):
    #     my_class_instance = Room()
    #     initial_room_count = len(my_class_instance.all_rooms)
    #     blue_office = my_class_instance.create_room("Blue", "office")
    #     self.assertTrue(blue_office)
    #     new_room_count = len(my_class_instance.all_rooms)
    #     self.assertEqual(new_room_count - initial_room_count, 1)
    #
    # def test_inputs_are_strings(self):
    #     # Test raises an error if either input is not a string
    #     with self.assertRaises(ValueError, msg='Only strings are allowed as input'):
    #         my_class_instance = Room()
    #         blue_office = my_class_instance.create_room(1234, "office")
