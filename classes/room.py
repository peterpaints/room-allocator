class Room(object):
    def __init__(self, room_name, room_type, max_persons):
        self.room_name = room_name
        self.room_type = room_type
        self.max_persons = max_persons
        self.persons = []


    def add_occupant(self, person):
        if len(self.persons) < self.max_persons:
            self.persons.append(person)
        else:
            return "Room is at full capacity"
