class Person(object):
    def __init__(self, person_type, person_name, person_surname="", wants_accommodation="N"):
        self.person_name = person_name
        self.person_surname = person_surname
        self.person_type = person_type
        self.wants_accommodation = wants_accommodation

    def full_name(self):
        self.full_name = self.person_name + " " + self.person_surname
        return self.full_name
