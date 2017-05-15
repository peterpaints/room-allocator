from classes.person import Person
# from person import Person


class Fellow(Person):
    def __init__(self, person_name, person_surname, wants_accommodation="N", person_type="fellow"):
        super(Fellow, self).__init__(person_type, person_name, person_surname, wants_accommodation)
