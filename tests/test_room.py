import unittest
from classes.room import Room
from classes.dojo import Dojo


class RoomClassTest(unittest.TestCase):
    def test_add_occupant(self):
        my_class_instance = Room("Blue", "office", 6)
        my_dojo_instance = Dojo()
        new_fellow = my_dojo_instance.add_person("fellow", "Peter", "Musonye", "Y")
        initial_persons_count = len(my_class_instance.persons)
        new_occupant = my_class_instance.add_occupant(new_fellow)
        # self.assertTrue(new_occupant)
        new_persons_count = len(my_class_instance.persons)
        self.assertEqual(new_persons_count - initial_persons_count, 1)

    def test_cannot_add_more_than_max_occupants(self):
        my_class_instance = Room("Blue", "office", 4)
        my_dojo_instance = Dojo()
        fellow_1 = my_dojo_instance.add_person("fellow", "Peter", "Musonye", "Y")
        fellow_2 = my_dojo_instance.add_person("staff", "Farhan", "Abdi")
        fellow_3 = my_dojo_instance.add_person("fellow", "Rose", "Maina", "Y")
        fellow_4 = my_dojo_instance.add_person("fellow", "Dennis", "Kola", "Y")
        fellow_5 = my_dojo_instance.add_person("fellow", "Eddy", "Karanja", "Y")
        occupant_1 = my_class_instance.add_occupant(fellow_1)
        occupant_2 = my_class_instance.add_occupant(fellow_2)
        occupant_3 = my_class_instance.add_occupant(fellow_3)
        occupant_4 = my_class_instance.add_occupant(fellow_4)
        occupant_5 = my_class_instance.add_occupant(fellow_5)
        self.assertEqual(occupant_5, "Room is at full capacity")
