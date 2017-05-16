import unittest
from classes.room import Room
from classes.dojo import Dojo


class RoomClassTest(unittest.TestCase):
    def setUp(self):
        self.my_class_instance = Room("Blue", "office", 4)
        self.my_dojo_instance = Dojo()

    def test_add_occupant(self):
        self.my_dojo_instance.add_person("fellow", "Peter", "Musonye", "Y")
        new_fellow = self.my_dojo_instance.all_persons[-1]
        initial_persons_count = len(self.my_class_instance.persons)
        self.my_class_instance.add_occupant(new_fellow)
        new_persons_count = len(self.my_class_instance.persons)
        self.assertEqual(new_persons_count - initial_persons_count, 1)

    def test_cannot_add_more_than_max_occupants(self):
        self.my_dojo_instance.add_person("fellow", "Peter", "Musonye", "Y")
        fellow_1 = self.my_dojo_instance.all_persons[-1]
        self.my_dojo_instance.add_person("fellow", "Farhan", "Abdi")
        fellow_2 = self.my_dojo_instance.all_persons[-1]
        self.my_dojo_instance.add_person("fellow", "Rose", "Maina", "Y")
        fellow_3 = self.my_dojo_instance.all_persons[-1]
        self.my_dojo_instance.add_person("fellow", "Dennis", "Kola", "Y")
        fellow_4 = self.my_dojo_instance.all_persons[-1]
        self.my_dojo_instance.add_person("fellow", "Eddy", "Karanja", "Y")
        fellow_5 = self.my_dojo_instance.all_persons[-1]
        self.my_class_instance.add_occupant(fellow_1)
        self.my_class_instance.add_occupant(fellow_2)
        self.my_class_instance.add_occupant(fellow_3)
        self.my_class_instance.add_occupant(fellow_4)
        with self.assertRaises(Exception, msg="Office Blue is at full capacity"):
            self.my_class_instance.add_occupant(fellow_5)
