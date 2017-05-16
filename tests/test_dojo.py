import unittest
from classes.dojo import Dojo


class DojoClassTest(unittest.TestCase):
    def setUp(self):
        self.my_class_instance = Dojo()

    def test_create_room_successfully(self):
        initial_room_count = len(self.my_class_instance.all_rooms)
        self.my_class_instance.create_room("office", "Blue")
        new_room_count = len(self.my_class_instance.all_rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_create_room_without_duplicates(self):
        self.my_class_instance.create_room("office", "Blue")
        self.my_class_instance.create_room("office", "Blue")
        self.assertEqual(len(self.my_class_instance.all_rooms), 1, msg="The same room can't be created twice")

    def test_inputs_create_room_are_strings(self):
        with self.assertRaises(ValueError, msg='Invalid: Please input a string as room_name or room_type'):
            self.my_class_instance.create_room(1234, "Blue")

    def test_add_person_successfully(self):
        initial_person_count = len(self.my_class_instance.all_persons)
        self.my_class_instance.add_person("staff", "Neil", "Armstrong", "Y")
        new_person_count = len(self.my_class_instance.all_persons)
        self.assertEqual(new_person_count - initial_person_count, 1)

    def test_inputs_add_person_are_strings(self):
        with self.assertRaises(ValueError, msg='Only strings are allowed as input'):
            self.my_class_instance.add_person("Fellow", "Peter", 23)

    def test_wants_accommodation_default_is_N(self):
        self.my_class_instance.add_person("Fellow", "Peter", "Musonye")
        result = self.my_class_instance.all_persons
        self.assertEqual(result[-1].wants_accommodation, 'n', msg="The default value of wants_accommodation is N if Y is not input")

    def test_person_type_either_fellow_or_staff(self):
        with self.assertRaises(ValueError, msg="Invalid person_type: Your person type should be either 'fellow' or 'staff'"):
            self.my_class_instance.add_person("Fella", "Peter", "Musonye")

    def test_wants_accommodation_is_Y_or_N(self):
        self.my_class_instance.add_person("Fellow", "Peter", "Musonye")
        result = self.my_class_instance.all_persons
        self.assertEqual(result[-1].wants_accommodation, 'n', msg="The default value of wants_accommodation is N if Y is not input")

    def test_allocation(self):
        """
        Test it actually allocates, by creating new room and fellow, calling
        allocate on them, then checking if that room has the fellow in its
        persons list.
        Also check if self.allocated_persons' length has increased.
        """
        self.my_class_instance.create_room("office", "Blue")
        new_office = self.my_class_instance.all_rooms[-1]
        self.my_class_instance.add_person("Fellow", "Peter", "Musonye")
        new_fellow = self.my_class_instance.all_persons[-1]
        self.my_class_instance.allocate_rooms()
        self.assertEqual(new_office.persons[-1], new_fellow)
        self.assertEqual(len(self.my_class_instance.allocated_persons), 1)
