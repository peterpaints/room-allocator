from classes.room import Room


class LivingSpace(Room):
    def __init__(self, room_name):
        super(LivingSpace, self).__init__(room_name, room_type="living_space", max_persons=4)

    def __repr__(self):
        pass
