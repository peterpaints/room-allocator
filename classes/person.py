from abc import ABCMeta, abstractmethod


class Person(metaclass=ABCMeta):

    def __init__(self, iden, person_type, person_name, person_surname="", wants_accommodation="N"):
        self.person_name = person_name
        self.person_surname = person_surname
        self.person_type = person_type
        self.wants_accommodation = wants_accommodation
        self.iden = iden

    @abstractmethod
    def __repr__(self):
        pass
