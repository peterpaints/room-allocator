import unittest
from classes.room import Room
from classes.dojo import Dojo


class RoomClassTest(unittest.TestCase):
    def setUp(self):
        self.my_class_instance = Room("Blue", "office", 4)
        self.my_dojo_instance = Dojo()

    def test_add_occupant(self):
        new_fellow = self.my_dojo_instance.add_person("fellow", "Peter", "Musonye", "Y")
        initial_persons_count = len(self.my_class_instance.persons)
        self.my_class_instance.add_occupant(new_fellow)
        new_persons_count = len(self.my_class_instance.persons)
        self.assertEqual(new_persons_count - initial_persons_count, 1)

    def test_cannot_add_more_than_max_occupants(self):
        fellow_1 = self.my_dojo_instance.add_person("fellow", "Peter", "Musonye", "Y")
        fellow_2 = self.my_dojo_instance.add_person("staff", "Farhan", "Abdi")
        fellow_3 = self.my_dojo_instance.add_person("fellow", "Rose", "Maina", "Y")
        fellow_4 = self.my_dojo_instance.add_person("fellow", "Dennis", "Kola", "Y")
        fellow_5 = self.my_dojo_instance.add_person("fellow", "Eddy", "Karanja", "Y")
        self.my_class_instance.add_occupant(fellow_1)
        self.my_class_instance.add_occupant(fellow_2)
        self.my_class_instance.add_occupant(fellow_3)
        self.my_class_instance.add_occupant(fellow_4)
        occupant_5 = self.my_class_instance.add_occupant(fellow_5)
        self.assertEqual(occupant_5, "Room is at full capacity")
