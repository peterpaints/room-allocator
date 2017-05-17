from classes.office import Office
from classes.living_space import LivingSpace
from classes.fellow import Fellow
from classes.staff import Staff
from random import randint


class Dojo(object):
    """
    This class imports Office, LivingSpace, Fellow and Staff.

    It creates instances of each in its methods.
    """

    def __init__(self):
        self.all_rooms = []
        self.allocated_persons = []
        self.unallocated_persons = []
        self.all_persons = []
        self.offices = []
        self.living_spaces = []

    def create_room(self, room_type, room_name):
        if not isinstance(room_name, str) or not isinstance(room_type, str):
            raise ValueError('Invalid: Please input a string as room_name or room_type')
        else:
            room_type = room_type.lower()
            room_name = room_name.lower()
        if room_type != "office" and room_type != "living_space":
            raise ValueError("Invalid room type: Your room type should be 'office' or 'living_space'")
        else:
            if room_type == 'office':
                room = Office(room_name)
            elif room_type == 'living_space':
                room = LivingSpace(room_name)
            try:
                for item in self.all_rooms:
                    if item.room_name == room_name and item.room_type == room_type:
                        raise Exception(room_type.title() + " " + room_name.title() + " already exists")
            except Exception as e:
                print (e)
            else:
                if room.room_type == 'office':
                    self.offices.append(room)
                elif room.room_type == 'living_space':
                    self.living_spaces.append(room)
                self.all_rooms.append(room)
                print ("An " + room.room_type + " called " + room.room_name.title() + " has been successfully created!")

    def add_person(self, person_type, person_name, person_surname, wants_accommodation="N"):
        if wants_accommodation:
            wants_accommodation = wants_accommodation.lower()
            if wants_accommodation != "y" and wants_accommodation != "n":
                raise ValueError("Please input Y or N for wants_accommodation")
        if not isinstance(person_type, str) or not isinstance(person_name, str) or not isinstance(person_surname, str):
            raise ValueError('Only strings are allowed as input')
        else:
            person_type = person_type.lower()
            person_name = person_name.lower()
            person_surname = person_surname.lower()
            if person_type != 'staff' and person_type != 'fellow':
                raise ValueError("Invalid person_type: Your person type should be either 'fellow' or 'staff'")
            if person_type == 'staff':
                person = Staff(person_name, person_surname)
            elif person_type == 'fellow':
                person = Fellow(person_name, person_surname, wants_accommodation)
            try:
                for item in self.all_persons:
                    if item.person_name == person_name and item.person_surname == person_surname:
                        raise Exception(person_type.title() + " " + person_name.title() + " already exists")
            except Exception as e:
                print (e)
            else:
                self.all_persons.append(person)
                print (person.person_type.title() + " " + person.person_name.title() + " " + person.person_surname.title() + " has been successfully added!")

    def allocate_rooms(self):
        if not self.all_persons:
            print ("There are no persons to allocate rooms")
        else:
            for person in self.all_persons:
                if person not in self.allocated_persons:
                    self.unallocated_persons.append(person)
                    if person.person_type == "fellow":
                        if person.wants_accommodation == "y":
                            if self.living_spaces:
                                random_living_space_number = randint(0, len(self.living_spaces) - 1)
                                living_space_allocation = self.living_spaces[random_living_space_number]
                                try:
                                    living_space_allocation.add_occupant(person)
                                except Exception as e:
                                    print (e)
                                self.allocated_persons.append(person)
                            else:
                                print ("There are no living_spaces to allocate " + person.person_name.title() + " " + person.person_surname.title())
                            if self.offices:
                                random_office_number = randint(0, len(self.offices) - 1)
                                office_allocation = self.offices[random_office_number]
                                try:
                                    office_allocation.add_occupant(person)
                                except Exception as e:
                                    print (e)
                                if person not in self.allocated_persons:
                                    self.allocated_persons.append(person)
                            else:
                                print ("There are no offices to allocate " + person.person_name.title() + " " + person.person_surname.title())
                        else:
                            if self.offices:
                                random_office_number = randint(0, len(self.offices) - 1)
                                office_allocation = self.offices[random_office_number]
                                try:
                                    office_allocation.add_occupant(person)
                                except Exception as e:
                                    print (e)
                                self.allocated_persons.append(person)
                            else:
                                print ("There are no offices to allocate " + person.person_name.title() + " " + person.person_surname.title())
                    elif person.person_type == "staff":
                        if self.offices:
                            random_office_number = randint(0, len(self.offices) - 1)
                            office_allocation = self.offices[random_office_number]
                            try:
                                office_allocation.add_occupant(person)
                            except Exception as e:
                                print (e)
                            self.allocated_persons.append(person)
                        else:
                            print ("There are no offices to allocate " + person.person_name.title() + " " + person.person_surname.title())
