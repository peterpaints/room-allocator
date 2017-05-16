import unittest
from classes.dojo import Dojo


class DojoClassTest(unittest.TestCase):
    def test_create_room_successfully(self):
        my_class_instance = Dojo()
        initial_room_count = len(my_class_instance.all_rooms)
        blue_office = my_class_instance.create_room("office", "Blue")
        new_room_count = len(my_class_instance.all_rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_create_room_without_duplicates(self):
        my_class_instance = Dojo()
        blue_office = my_class_instance.create_room("office", "Blue")
        another_office = my_class_instance.create_room("office", "Blue")
        self.assertEqual(another_office, "Room already exists", msg="The same room can't be created twice")

    def test_inputs_create_room_are_strings(self):
        # Test raises an error if either input is not a string
        with self.assertRaises(ValueError, msg='Only strings are allowed as input'):
            my_class_instance = Dojo()
            blue_office = my_class_instance.create_room(1234, "Blue")

    def test_add_person_successfully(self):
        my_class_instance = Dojo()
        initial_person_count = len(my_class_instance.all_persons)
        staff_neil = my_class_instance.add_person("staff", "Neil", "Armstrong", "Y")
        new_person_count = len(my_class_instance.all_persons)
        self.assertEqual(new_person_count - initial_person_count, 1)

    def test_inputs_add_person_are_strings(self):
        with self.assertRaises(ValueError, msg='Only strings are allowed as input'):
            my_class_instance = Dojo()
            my_class_instance.add_person("Fellow", "Peter", 23)

    def test_wants_accommodation_default_is_N(self):
        my_class_instance = Dojo()
        my_class_instance.add_person("Fellow", "Peter", "Musonye")
        result = my_class_instance.all_persons
        self.assertEqual(result[0].wants_accommodation, 'N', msg="The default value of wants_accommodation is N if Y is not input")

    def test_person_type_either_fellow_or_staff(self):
        my_class_instance = Dojo()
        attempt = my_class_instance.add_person("Fella", "Peter", "Musonye")
        self.assertEqual(attempt, "Invalid person_type", msg="The person type should be either fellow or staff. Person was not added")

    def test_wants_accommodation_is_Y_or_N(self):
        my_class_instance = Dojo()
        my_class_instance.add_person("Fellow", "Peter", "Musonye", "Yes")
        result = my_class_instance.all_persons
        self.assertEqual(result[0].wants_accommodation, 'N', msg="The default value of wants_accommodation is N if Y is not input")

    def test_allocation(self):
        # test it actually allocates, by creating new room and fellow, calling
        # allocate on them, then checking if that room has the fellow in its
        # persons list.
        my_class_instance = Dojo()
        my_class_instance.create_room("office", "Blue")
        new_office = my_class_instance.all_rooms[-1]
        my_class_instance.add_person("Fellow", "Peter", "Musonye")
        new_fellow = my_class_instance.all_persons[-1]
        my_class_instance.allocate_rooms()
        self.assertEqual(new_office.persons[-1], new_fellow)

    def test_allocated_persons_length_increases_once_person_is_allocated(self):
        # Check if self.allocated_persons's length has increased.
        my_class_instance = Dojo()
        my_class_instance.create_room("office", "Blue")
        new_office = my_class_instance.all_rooms[-1]
        my_class_instance.add_person("Fellow", "Peter", "Musonye")
        new_fellow = my_class_instance.all_persons[-1]
        my_class_instance.allocate_rooms()
        self.assertEqual(len(my_class_instance.allocated_persons), 1)
