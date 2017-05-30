from classes.person import Person


class Fellow(Person):
    def __init__(self, iden, person_name, person_surname, wants_accommodation="N", person_type="fellow"):
        super(Fellow, self).__init__(iden, person_type, person_name, person_surname, wants_accommodation)
