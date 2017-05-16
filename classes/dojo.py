from classes.office import Office
from classes.living_space import LivingSpace
from classes.fellow import Fellow
from classes.staff import Staff
from random import randint
# from office import Office
# from living_space import LivingSpace
# from fellow import Fellow
# from staff import Staff


class Dojo(object):
    def __init__(self):
        self.all_rooms = []
        self.allocated_persons = []
        self.unallocated_persons = []
        self.all_persons = []
        self.offices = []
        self.living_spaces = []

    def create_room(self, room_type, room_name):
        if not isinstance(room_name, str) or not isinstance(room_type, str):
            raise ValueError('Only strings are allowed as input')
        else:
            room_type = room_type.lower()
            room_name = room_name.lower()
        if room_type != "office" and room_type != "living_space":
            raise ValueError("Invalid office type: Either 'office' or 'living_space'")
        for room in self.all_rooms:
            if room.room_name == room_name and room.room_type == room_type:
                return "Room already exists"

        if room_type == 'office':
            room = Office(room_name)
            self.offices.append(room)
        elif room_type == 'living_space':
            room = LivingSpace(room_name)
            self.living_spaces.append(room)
        self.all_rooms.append(room)
        print ("An " + room.room_type + " called " + room.room_name.title() + " has been successfully created!")

    def add_person(self, person_type, person_name, person_surname, wants_accommodation="N"):
        if not isinstance(person_type, str) or not isinstance(person_name, str) or not isinstance(person_surname, str) or not isinstance(wants_accommodation, str):
            raise ValueError('Only strings are allowed as input')
        else:
            person_type = person_type.lower()
            person_name = person_name.lower()
            person_surname = person_surname.lower()
            if person_type != 'staff' and person_type != 'fellow':
                return "Invalid person_type"
            if person_type == 'staff':
                person = Staff(person_name, person_surname)
                # self.all_persons.append(person)
                # print (person.person_type.title() + " " + person.person_name.title() + " " + person.person_surname.title() + " has been successfully added!")
            elif person_type == 'fellow':
                if wants_accommodation == "Y":
                    person = Fellow(person_name, person_surname, wants_accommodation)
                else:
                    person = Fellow(person_name, person_surname)
            self.all_persons.append(person)
            print (person.person_type.title() + " " + person.person_name.title() + " " + person.person_surname.title() + " has been successfully added!")

    def allocate_rooms(self):
        for person in self.all_persons:
            if person.person_type == "fellow":
                if person.wants_accommodation == "Y":
                    if self.living_spaces:
                        random_living_space_number = randint(0, len(self.living_spaces) - 1)
                        living_space_allocation = self.living_spaces[random_living_space_number]
                        living_space_allocation.add_occupant(person)
                        print (person.person_type.title() + " " + person.person_name.title() + " " + person.person_surname.title() + " has been allocated " + living_space_allocation.room_type + " " + living_space_allocation.room_name.title())
                    else:
                        print ("There are no living_spaces")
                    if self.offices:
                        random_office_number = randint(0, len(self.offices) - 1)
                        office_allocation = self.offices[random_office_number]
                        office_allocation.add_occupant(person)
                        print (person.person_type.title() + " " + person.person_name.title() + " " + person.person_surname.title() + " has been allocated " + office_allocation.room_type + " " + office_allocation.room_name.title())
                    else:
                        print ("There are no offices")

                    for room in self.all_rooms:
                        if person in room.persons:
                            self.allocated_persons.append(person)
                else:
                    if self.offices:
                        random_office_number = randint(0, len(self.offices) - 1)
                        office_allocation = self.offices[random_office_number]
                        office_allocation.add_occupant(person)
                        self.allocated_persons.append(person)
                        print (person.person_type.title() + " " + person.person_name.title() + " " + person.person_surname.title() + " has been allocated " + office_allocation.room_type + " " + office_allocation.room_name.title())
                    else:
                        print ("There are no offices")
            elif person.person_type == "staff":
                if self.offices:
                    random_office_number = randint(0, len(self.offices) - 1)
                    office_allocation = self.offices[random_office_number]
                    office_allocation.add_occupant(person)
                    self.allocated_persons.append(person)
                    print (person.person_type.title() + " " + person.person_name.title() + " " + person.person_surname.title() + " has been allocated " + office_allocation.room_type + " " + office_allocation.room_name.title())
                else:
                    print ("There are no offices")

            for person in self.all_persons:
                if person not in self.allocated_persons:
                    self.unallocated_persons.append(person)


# my_class_instance = Dojo()
# new_office = my_class_instance.create_room("office", "Blue")
# new_living_space = my_class_instance.create_room("living_space", "Hogwarts")
# another_office = my_class_instance.create_room("office", "Blue")
# print (new_office)
# print (new_living_space)
# print (another_office)
# for room in my_class_instance.all_rooms:
#     print (room.room_type, room.room_name)
# x = Dojo()
# new_fellow = x.add_person("fellow", "Peter", "Musonye", "Y")
# print (x.allocate_rooms(new_fellow))
