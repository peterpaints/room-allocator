import os
import sys
import unittest
from io import StringIO
from classes.dojo import Dojo


class DojoClassTest(unittest.TestCase):
    def setUp(self):
        self.my_class_instance = Dojo()
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_create_room_successfully(self):
        """Test that the list of all rooms increases by 1."""
        initial_room_count = len(self.my_class_instance.all_rooms)
        self.my_class_instance.create_room("office", "Blue")
        new_room_count = len(self.my_class_instance.all_rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_create_room_without_duplicates(self):
        """Test that a room cannot be created twice."""
        self.my_class_instance.create_room("office", "Blue")
        self.my_class_instance.create_room("office", "Blue")
        self.assertEqual(len(self.my_class_instance.all_rooms), 1, msg="The same room can't be created twice")

    def test_add_person_successfully(self):
        """Test that the list of all persons increases by one."""
        initial_person_count = len(self.my_class_instance.all_persons)
        self.my_class_instance.add_person("staff", "Neil", "Armstrong", "Y")
        new_person_count = len(self.my_class_instance.all_persons)
        self.assertEqual(new_person_count - initial_person_count, 1)

    def test_wants_accommodation_default_is_N(self):
        """Test that the option for wants_accommodation has a default of N."""
        self.my_class_instance.add_person("Fellow", "Peter", "Musonye")
        result = self.my_class_instance.all_persons
        self.assertEqual(result[-1].wants_accommodation, 'n', msg="The default value of wants_accommodation is N if Y is not input")

    def test_person_type_either_fellow_or_staff(self):
        """Test that person_type is either 'fellow' or 'staff'."""
        self.my_class_instance.add_person("Fella", "Peter", "Musonye")
        message = sys.stdout.getvalue().strip()
        self.assertIn("Invalid person_type: Your person type should be either 'fellow' or 'staff'", message)

    def test_wants_accommodation_is_Y_or_N(self):
        """Test that wants_accommodation is only 'Y' or 'N'."""
        self.my_class_instance.add_person("Fellow", "Peter", "Musonye", "Yes")
        message = sys.stdout.getvalue().strip()
        self.assertIn("Please input Y or N for wants_accommodation", message)

    def test_allocation(self):
        """
        Test that it actually allocates, by creating new room and fellow.

        Call allocate on them, then check if that room has the fellow in its persons list.
        Also check if self.allocated_persons' length has increased.
        """
        self.my_class_instance.create_room("office", "Blue")
        new_office = self.my_class_instance.all_rooms[-1]
        self.my_class_instance.add_person("Fellow", "Peter", "Musonye")
        new_fellow = self.my_class_instance.all_persons[-1]
        self.my_class_instance.allocate_rooms()
        self.assertEqual(new_office.persons[-1], new_fellow)
        self.assertEqual(len(self.my_class_instance.those_allocated_offices), 1)

    def test_that_rooms_must_exist_to_be_printed(self):
        """Test that error message is output if room does not exist."""
        self.my_class_instance.print_room("black")
        message = sys.stdout.getvalue().strip()
        self.assertIn("Black does not exist", message)

    def test_it_outputs_message_if_room_has_no_allocations(self):
        """Test that message is printed if a room has no occupants."""
        self.my_class_instance.create_room("office", "Black")
        new_office = self.my_class_instance.all_rooms[-1]
        self.my_class_instance.allocate_rooms()
        self.my_class_instance.print_room(new_office.room_name)
        message = sys.stdout.getvalue().strip()
        self.assertIn("Office Black has no occupants", message)

    def test_it_outputs_correct_occupants(self):
        """Test that actual occupants only are printed."""
        self.my_class_instance.add_person("fellow", "Peter", "Musonye")
        self.my_class_instance.add_person("staff", "Peter", "Muriuki")
        self.my_class_instance.create_room("office", "Black")
        new_office = self.my_class_instance.all_rooms[-1]
        self.my_class_instance.allocate_rooms()
        new_office_occupants = self.my_class_instance.print_room(new_office.room_name)
        allocations = self.my_class_instance.print_allocations()
        self.my_class_instance.print_unallocated()
        message = sys.stdout.getvalue().strip()
        self.assertEqual(new_office_occupants, ["Peter Musonye Fellow ID: 1", "Peter Muriuki Staff ID: 2"])
        self.assertEqual(allocations, ["Peter Musonye Fellow ID: 1", "Peter Muriuki Staff ID: 2"])
        self.assertIn("Everyone has been allocated a room", message)

    def test_print_allocations_to_file(self):
        """Test for correct allocations in file if optioned."""
        self.my_class_instance.add_person("fellow", "Peter", "Musonye")
        self.my_class_instance.add_person("staff", "Peter", "Muriuki")
        self.my_class_instance.create_room("office", "Black")
        self.my_class_instance.allocate_rooms()
        self.my_class_instance.print_allocations("test1")
        f = open("test1.txt").readlines()
        self.assertEqual(f[1], "Office Black:\n")
        self.assertEqual(f[3], "Peter Musonye Fellow ID: 1\n")
        self.assertEqual(f[4], "Peter Muriuki Staff ID: 2\n")
        os.remove("test1.txt")

    def test_print_unallocated_to_file(self):
        """Test for correct output in unallocated persons file if optioned."""
        self.my_class_instance.add_person("fellow", "Peter", "Musonye", "y")
        self.my_class_instance.add_person("fellow", "John", "Doe", "y")
        self.my_class_instance.add_person("fellow", "Barack", "Obama", "y")
        self.my_class_instance.add_person("fellow", "Hilary", "Clinton", "y")
        self.my_class_instance.add_person("fellow", "The", "Donald", "y")
        self.my_class_instance.create_room("living_space", "Buckingham")
        self.my_class_instance.allocate_rooms()
        self.my_class_instance.print_unallocated("test2")
        f = open("test2.txt").readlines()
        self.assertEqual(f[0], "The Donald Fellow ID: 5\n")
        os.remove("test2.txt")

    def test_it_reallocates_as_specified(self):
        """Test that once reallocated, the person is only in one list of occupants, that of the new room."""
        self.my_class_instance.add_person("fellow", "Peter", "Musonye")
        self.my_class_instance.create_room("office", "Black")
        black_office = self.my_class_instance.all_rooms[-1]
        self.my_class_instance.allocate_rooms()
        black_office_occupants = self.my_class_instance.print_room(black_office.room_name)
        self.assertEqual(black_office_occupants, ["Peter Musonye Fellow ID: 1"])
        self.my_class_instance.create_room("office", "Blue")
        self.my_class_instance.reallocate_person(1, "office", "Blue")
        blue_office = self.my_class_instance.all_rooms[-1]
        black_office_occupants = self.my_class_instance.print_room(black_office.room_name)
        blue_office_occupants = self.my_class_instance.print_room(blue_office.room_name)
        self.assertEqual(black_office_occupants, [])
        self.assertEqual(blue_office_occupants, ["Peter Musonye Fellow ID: 1"])

    def test_cannot_reallocate_to_non_existent_room(self):
        """Test that reallocation only happens with rooms in the system."""
        self.my_class_instance.reallocate_person(5, "office", "Capitol")
        message = sys.stdout.getvalue().strip()
        self.assertIn("Office Capitol does not exist", message)

    def test_raises_error_if_reallocating_to_full_room(self):
        """Test that an error is raised when reallocating to a full room."""
        self.my_class_instance.add_person("fellow", "Peter", "Musonye", "y")
        self.my_class_instance.add_person("fellow", "John", "Doe", "y")
        self.my_class_instance.add_person("fellow", "Bar", "Obama", "y")
        self.my_class_instance.add_person("fellow", "Hilary", "Clinton", "y")
        self.my_class_instance.create_room("living_space", "Capitol")
        self.my_class_instance.allocate_rooms()
        self.my_class_instance.add_person("fellow", "The", "Donald", "y")
        self.my_class_instance.create_room("living_space", "TrumpTower")
        self.my_class_instance.allocate_rooms()
        self.my_class_instance.reallocate_person(5, "living_space", "Capitol")
        message = sys.stdout.getvalue().strip()
        self.assertIn("Living_Space Capitol is at full capacity", message)

    def test_cannot_reallocate_non_existent_person(self):
        """Test that reallocation only happens with people in the system."""
        self.my_class_instance.create_room("office", "Capitol")
        self.my_class_instance.reallocate_person(5, "office", "Capitol")
        message = sys.stdout.getvalue().strip()
        self.assertIn("ID 5 has not been allocated an office yet", message)

    def test_raises_error_for_wrong_room_type_or_name(self):
        """Test that room_type is only 'office' or 'living_space'."""
        self.my_class_instance.reallocate_person(5, "living", "Capitol")
        message = sys.stdout.getvalue().strip()
        self.assertIn("Invalid room type: Your room type should be 'office' or 'living_space'", message)

    def test_load_people(self):
        """Test that people can be added from a txt file correctly."""
        f = open("test3.txt", "a")
        f.write("OLUWAFEMI SULE FELLOW Y" + "\n")
        f.write("DOMINIC WALTERS STAFF" + "\n")
        f.write("SIMON PATTERSON FELLOW Y" + "\n")
        f.write("MARI LAWRENCE FELLOW Y" + "\n")
        f.write("LEIGH RILEY STAFF" + "\n")
        f.write("TANA LOPEZ FELLOW Y" + "\n")
        f.write("KELLY McGUIRE STAFF" + "\n")
        f.close()
        self.my_class_instance.load_people("test3")
        people = self.my_class_instance.all_persons
        person_count = len(people)
        self.assertListEqual([people[0].person_name, people[0].person_surname], ["oluwafemi", "sule"])
        self.assertListEqual([people[6].person_name, people[6].person_surname], ["kelly", "mcguire"])
        self.assertEqual(person_count, 7)
        os.remove("test3.txt")

    def test_save_state(self):
        """Test that current app data is stored correctly in db specified."""
        pass
