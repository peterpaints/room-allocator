import unittest
from classes.dojo import Dojo


class RoomClassTest(unittest.TestCase):
    def setUp(self):
        self.dojo = Dojo()

    def test_add_occupant(self):
        """Test that the list of persons actually increases."""
        self.dojo.add_person("fellow", "Peter", "Musonye", "Y")
        new_fellow = self.dojo.all_persons[-1]
        self.dojo.create_room("office", "blue")
        new_room = self.dojo.all_rooms[-1]
        new_room.add_occupant(new_fellow)
        self.assertEqual(len(new_room.persons), 1)

    def test_add_occupant_more_than_max_(self):
        """Test that occupants cannot be added to a full room."""
        self.dojo.add_person("fellow", "Peter", "Musonye", "Y")
        fellow_1 = self.dojo.all_persons[-1]
        self.dojo.add_person("fellow", "Farhan", "Abdi", "Y")
        fellow_2 = self.dojo.all_persons[-1]
        self.dojo.add_person("fellow", "Rose", "Maina", "Y")
        fellow_3 = self.dojo.all_persons[-1]
        self.dojo.add_person("fellow", "Dennis", "Kola", "Y")
        fellow_4 = self.dojo.all_persons[-1]
        self.dojo.add_person("fellow", "Eddy", "Karanja", "Y")
        fellow_5 = self.dojo.all_persons[-1]
        self.dojo.create_room("living_space", "havana")
        new_room = self.dojo.all_rooms[-1]
        new_room.add_occupant(fellow_1)
        new_room.add_occupant(fellow_2)
        new_room.add_occupant(fellow_3)
        new_room.add_occupant(fellow_4)
        with self.assertRaises(Exception, msg="Living_Space Havana is at full capacity"):
            new_room.add_occupant(fellow_5)

    def test_add_occupant_already_in_room(self):
        """Test that the same occupant cannot be added to a room again."""
        self.dojo.add_person("fellow", "Peter", "Musonye", "Y")
        fellow_1 = self.dojo.all_persons[-1]
        self.dojo.create_room("living_space", "havana")
        new_room = self.dojo.all_rooms[-1]
        new_room.add_occupant(fellow_1)
        with self.assertRaises(Exception, msg="Fellow Peter Musonye is already among the occupants in Living_Space Havana"):
            new_room.add_occupant(fellow_1)
