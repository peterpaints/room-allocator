from classes.person import Person


class Staff(Person):
    def __init__(self, iden, person_name, person_surname, person_type="staff"):
        super(Staff, self).__init__(iden, person_type, person_name, person_surname, wants_accommodation="N")
