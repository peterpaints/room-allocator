from abc import ABCMeta, abstractmethod
from termcolor import cprint


class Room(metaclass=ABCMeta):
    def __init__(self, room_name, room_type, max_persons):
        self.room_name = room_name
        self.room_type = room_type
        self.max_persons = max_persons
        self.persons = []

    def add_occupant(self, person):
        """
        Append person objects to self.persons.

        However, len(self.persons) must be below the value of max_persons and
        the person object being appended must not exist in self.persons
        """
        if person not in self.persons:
            if len(self.persons) < self.max_persons:
                self.persons.append(person)
                cprint("\n" + person.person_type.title() + " " + person.person_name.title() + " " + person.person_surname.title() + " has been allocated " + self.room_type + " " + self.room_name.title(), 'cyan', attrs=['dark'])
            else:
                raise Exception(self.room_type.title() + " " + self.room_name.title() + " is at full capacity")
        else:
            raise Exception(person.person_type.title() + " " + person.person_name.title() + " " + person.person_surname.title() + " is already among the occupants in " + self.room_type + " " + self.room_name.title())

    @abstractmethod
    def __repr__(self):
        pass
