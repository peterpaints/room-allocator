class Room(object):
    def __init__(self, room_name, room_type, max_persons):
        self.room_name = room_name
        self.room_type = room_type
        self.max_persons = max_persons
        self.persons = []

    def add_occupant(self, person):
        if person not in self.persons:
            if len(self.persons) < self.max_persons:
                self.persons.append(person)
                print (person.person_type.title() + " " + person.person_name.title() + " " + person.person_surname.title() + " has been allocated " + self.room_type + " " + self.room_name.title())
            else:
                raise Exception(self.room_type.title() + " " + self.room_name.title() + " is at full capacity")
        else:
            raise Exception(person.person_type.title() + " " + person.person_name.title() + " " + person.person_surname.title() + " is already among the occupants in " + self.room_type + " " + self.room_name.title())
