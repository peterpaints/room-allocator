from classes.room import Room
# from room import Room

class LivingSpace(Room):
    def __init__(self, room_name):
        super(LivingSpace, self).__init__(room_name, room_type="living_space", max_persons=4)


# x = LivingSpace("palace")
# print (x.persons)
# print (x.add_occupant("Peter"))
# print (x.persons)
