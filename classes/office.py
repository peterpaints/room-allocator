from classes.room import Room


class Office(Room):
    def __init__(self, room_name):
        super(Office, self).__init__(room_name, room_type="office", max_persons=6)

    def __repr__(self):
        pass
