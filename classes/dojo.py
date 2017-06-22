import os
import random
import sys

from classes.db import Base, People, Rooms
from classes.office import Office
from classes.living_space import LivingSpace
from classes.fellow import Fellow
from classes.staff import Staff
from io import StringIO
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from termcolor import cprint


class Dojo(object):
    """
    This class imports Office, LivingSpace, Fellow and Staff.

    It creates instances of each in its methods.
    """

    def __init__(self):
        self.all_rooms = []
        self.all_persons = []
        self.offices = []
        self.living_spaces = []
        self.those_allocated_offices = []
        self.those_allocated_living_spaces = []
        self.iden = 0

    def create_room(self, room_type, room_name):
        """
        Create an instance of either Office() or LivingSpace().

        It then appends it first to self.all_rooms, then to either self.offices
        or self.living_spaces, depending on the room_type input.
        """
        room_type = room_type.lower()
        room_name = room_name.lower()
        if room_type != "office" and room_type != "living_space":
            cprint("\n" + "Invalid room type: Your room type should be 'office' or 'living_space'", 'red', attrs=['dark'])
        elif room_name.isnumeric():
            cprint("\n" + "Invalid room name: Your room name should be alphanumeric", 'red', attrs=['dark'])
        else:
            if room_type == 'office':
                room = Office(room_name)
            elif room_type == 'living_space':
                room = LivingSpace(room_name)
            try:
                for item in self.all_rooms:
                    if item.room_name == room_name and item.room_type == room_type:
                        raise Exception(
                            room_type.title() + " " + room_name.title() + " already exists")
            except Exception as e:
                cprint("\n" + str(e), 'red', attrs=['dark'])
            else:
                if room.room_type == 'office':
                    self.offices.append(room)
                elif room.room_type == 'living_space':
                    self.living_spaces.append(room)
                self.all_rooms.append(room)
                cprint("\n" + "An " + room.room_type + " called " +
                       room.room_name.title() + " has been successfully created!", 'green', attrs=['dark'])

    def add_person(self, person_type, person_name, person_surname, wants_accommodation="N"):
        """
        Create an instance of either Fellow() or Staff().

        This depends on the person_type input.
        This object is then appended to self.all_persons
        """
        wants_accommodation = wants_accommodation.lower()
        person_type = person_type.lower()
        person_name = person_name.lower()
        person_surname = person_surname.lower()
        if wants_accommodation != "y" and wants_accommodation != "n":
            cprint("\n" + "Please input Y or N for wants_accommodation", 'red', attrs=['dark'])
        elif person_type != 'staff' and person_type != 'fellow':
            cprint("\n" + "Invalid person_type: Your person type should be either 'fellow' or 'staff'", 'red', attrs=['dark'])
        elif person_name.isnumeric() or person_surname.isnumeric():
            cprint("\n" + "Invalid name: Names should be alphanumeric", 'red', attrs=['dark'])
        else:
            id_range = range(0, 10000)
            if person_type == 'staff':
                self.iden += random.choice(id_range)
                person = Staff(self.iden, person_name, person_surname)
            elif person_type == 'fellow':
                self.iden += random.choice(id_range)
                person = Fellow(
                    self.iden, person_name, person_surname, wants_accommodation)
            try:
                for item in self.all_persons:
                    if item.person_name == person_name and item.person_surname == person_surname:
                        raise Exception(
                            person_type.title() + " " + person_name.title() + " already exists")
            except Exception as e:
                cprint("\n" + str(e), 'red', attrs=['dark'])
            else:
                self.all_persons.append(person)
                cprint("\n" + person.person_type.title() + " " + person.person_name.title() +
                       " " + person.person_surname.title() + " " + "ID: " + str(person.iden) + " has been successfully added!", 'green', attrs=['dark'])

    def allocate_rooms(self):
        """
        Choose a room at random, and call that room's add_occupant method.

        If the add_occupant method returns an error, either because the room is
        full, or the person in the current iteration is already in its list of
        occupants, then restart the loop, so as to choose another room.
        Since this might result in the same room being chosen, this allocation
        needs to be 'tried' a number of times, hence the while loop.
        """
        if not self.all_persons:
            cprint("\n" + "There are no persons to allocate rooms", 'magenta', attrs=['dark'])
        else:
            tries = 3 + len(self.all_rooms) * 20
            while tries > 0:
                for person in self.all_persons:
                    tries -= 1
                    if person.person_type == "fellow" and person.wants_accommodation == "y":
                        if person not in self.those_allocated_living_spaces:
                            if self.living_spaces:
                                living_space_allocation = random.choice(self.living_spaces)
                                try:
                                    living_space_allocation.add_occupant(
                                        person)
                                    self.those_allocated_living_spaces.append(person)
                                except Exception:
                                    pass
                        if person not in self.those_allocated_offices:
                            if self.offices:
                                office_allocation = random.choice(self.offices)
                                try:
                                    office_allocation.add_occupant(
                                        person)
                                    self.those_allocated_offices.append(person)
                                except Exception:
                                    continue
                    elif person.person_type == "fellow" and person.wants_accommodation != "y":
                        if person not in self.those_allocated_offices:
                            if self.offices:
                                office_allocation = random.choice(self.offices)
                                try:
                                    office_allocation.add_occupant(
                                        person)
                                    self.those_allocated_offices.append(person)
                                except Exception:
                                    continue
                    elif person.person_type == "staff":
                        if person not in self.those_allocated_offices:
                            if self.offices:
                                office_allocation = random.choice(self.offices)
                                try:
                                    office_allocation.add_occupant(
                                        person)
                                    self.those_allocated_offices.append(person)
                                except Exception:
                                    continue

    def print_room(self, room_name):
        """
        Match room_name with the corresponding room in all_rooms.

        Then loop through that rooms occupants, printing each one to a new line
        """
        room_name = room_name.lower()
        found = False
        for room in self.all_rooms:
            room_occupants = []
            if room.room_name == room_name:
                found = True
                cprint("\n" + room.room_type.title() +
                       " " + room_name.title() + ":" + "\n", 'cyan', attrs=['underline'])
                if not room.persons:
                    cprint(room.room_type.title(
                    ) + " " + room.room_name.title() + " " + "has no occupants", 'green', attrs=['dark'])
                else:
                    for occupant in room.persons:
                        room_occupants.append(occupant.person_name.title(
                        ) + " " + occupant.person_surname.title() + " " + occupant.person_type.title() + " ID: " + str(occupant.iden))
                for occupant in room_occupants:
                    cprint (occupant, 'green', attrs=['dark'])
        if not found:
            cprint("\n" + room_name.title() + " does not exist", 'red', attrs=['dark'])
        else:
            return room_occupants

    def print_allocations(self, filename=None):
        """For each room, print out room title, followed by a list of occupants."""
        if not self.all_rooms:
            cprint("\nThere are no allocations yet", 'red', attrs=['dark'])
        else:
            if filename:
                cprint("\nOutput written to " + filename + ".txt", 'green', attrs=['dark'])
            for room in self.all_rooms:
                room_occupants = []
                if not room.persons:
                    room_occupants.append(room.room_type.title() + " " + room.room_name.title() + " " + "has no occupants")
                for occupant in room.persons:
                    room_occupants.append(occupant.person_name.title(
                    ) + " " + occupant.person_surname.title() + " " + occupant.person_type.title() + " ID: " + str(occupant.iden))
                if filename:
                    filename = filename.lower()
                    f = open(filename + ".txt", "a")
                    f.write(" " + "\n")
                    f.write(room.room_type.title() + " " +
                            room.room_name.title() + ":" + "\n")
                    f.write("-" * 23 + "\n")
                    for occupant in room_occupants:
                        f.write(occupant + "\n")
                else:
                    print (" ")
                    cprint(room.room_type.title() + " " +
                           room.room_name.title() + ":", 'cyan', attrs=['dark'])
                    print ("-" * 23)
                    for occupant in room_occupants:
                        cprint(occupant, 'green', attrs=['dark'])
            return room_occupants

    def print_unallocated(self, filename=None):
        """
        Check if a person is not in either of the following lists.

        Self.those_allocated_offices and self.those_allocated_living_spaces, so
        print them out.
        """
        found = False
        print (" ")
        for person in self.all_persons:
            if person not in self.those_allocated_offices and person not in self.those_allocated_living_spaces:
                found = True
                if filename:
                    filename = filename.lower()
                    f = open(filename + ".txt", "a")
                    f.write(person.person_name.title(
                    ) + " " + person.person_surname.title() + " " + person.person_type.title() + " ID: " + str(person.iden) + "\n")
                else:
                    cprint(person.person_name.title() + " " + person.person_surname.title() + " " + person.person_type.title() + " ID: " + str(person.iden), 'green', attrs=['dark'])
        if not found:
            if not self.all_persons:
                cprint("There's no one in the system", 'red', attrs=['dark'])
            else:
                cprint("Everyone has been allocated a room", 'cyan', attrs=['dark'])
        else:
            if filename:
                cprint("Output written to " + filename + ".txt", 'green', attrs=['dark'])

    def reallocate_person(self, iden, room_type, room_name):
        """
        Match iden and room_name to a person and room in the system.

        First call add_occupant in the new room, then if successful, remove
        the reallocated person from his previous room.
        """
        if not iden.isnumeric():
            cprint("\n" + "Invalid ID: Please use a numeric ID", 'red', attrs=['dark'])
        elif room_type != "office" and room_type != "living_space":
            cprint("\n" + "Invalid room type: Your room type should be 'office' or 'living_space'", 'red', attrs=['dark'])
        else:
            iden = int(iden)
            room_type = room_type.lower()
            room_name = room_name.lower()
            new_allocation = object
            person_found = False

            if room_type == "office":
                office_found = False
                for office in self.offices:
                    if office.room_name == room_name:
                        office_found = True
                        new_allocation = office

                for person in self.those_allocated_offices:
                    if person.iden == iden:
                        person_found = True
                        our_guy = person

                if not office_found:
                    cprint("\n" + "Office " + room_name.title() + " does not exist", 'red', attrs=['dark'])
                elif not person_found:
                    cprint("\n" + "ID " + str(iden) + " has not been allocated an office yet", 'red', attrs=['dark'])
                else:
                    try:
                        new_allocation.add_occupant(our_guy)
                    except Exception as e:
                        cprint("\n" + str(e), 'red', attrs=['dark'])
                    else:
                        for room in self.offices:
                            for occupant in room.persons:
                                if occupant == our_guy and room.room_name != room_name:
                                    room.persons.remove(our_guy)

            elif room_type == "living_space":
                living_space_found = False
                for living_space in self.living_spaces:
                    if living_space.room_name == room_name:
                        living_space_found = True
                        new_allocation = living_space

                for person in self.those_allocated_living_spaces:
                    if person.iden == iden:
                        person_found = True
                        our_guy = person

                if not living_space_found:
                    cprint("\n" + "Living Space " + room_name.title() + " does not exist", 'red', attrs=['dark'])
                elif not person_found:
                    cprint("\n" + "ID " + str(iden) + " has not been allocated a living_space yet", 'red', attrs=['dark'])
                else:
                    try:
                        new_allocation.add_occupant(our_guy)
                    except Exception as e:
                        cprint("\n" + str(e), 'red', attrs=['dark'])
                    else:
                        for room in self.living_spaces:
                            for occupant in room.persons:
                                if occupant == our_guy and room.room_name != room_name:
                                    room.persons.remove(our_guy)

    def load_people(self, filename):
        """
        Read each line from the specified txt file, and split it into a list.

        Call self.add_person with the various items in that list as arguments.
        """
        filename = filename.lower()
        try:
            f = open(filename + ".txt").readlines()
            for person in f:
                person = person.split()
                try:
                    self.add_person(person[2], person[0], person[1], person[3])
                    self.allocate_rooms()
                except Exception:
                    self.add_person(person[2], person[0], person[1])
                    self.allocate_rooms()
        except FileNotFoundError:
            cprint("\n" + filename + ".txt not found", 'red', attrs=['dark'])

    def save_state(self, db=None):
        """Save data in self.all_rooms and self.all_persons to an sqlite3 db."""
        if db:
            db = db.lower()
            db = db + '.sqlite'
        else:
            db = 'default.sqlite'

        engine = create_engine('sqlite:///' + db)
        Session = sessionmaker()
        Session.configure(bind=engine)
        Base.metadata.create_all(engine)

        Base.metadata.bind = engine

        session = Session()

        if not self.all_persons and not self.all_rooms:
            cprint("\n" + "There was no data to save to " + db, 'green', attrs=['dark'])
        else:
            for person in self.all_persons:
                new_person = People(
                    iden=person.iden,
                    person_name=person.person_name,
                    person_surname=person.person_surname,
                    person_type=person.person_type,
                    wants_accommodation=person.wants_accommodation
                    )
                session.merge(new_person)

            for room in self.all_rooms:
                new_room = Rooms(
                    room_name=room.room_name,
                    room_type=room.room_type,
                    room_persons=", ".join([str(person.iden) for person in room.persons])
                    )
                session.merge(new_room)

            session.commit()
            cprint("\n" + "Data saved to " + db + " successfully", 'green', attrs=['dark'])

    def load_state(self, db):
        """Query data from specified db and reconstruct people and allocations."""
        db = db.lower()
        if not os.path.exists(db + '.sqlite'):
            cprint("\n" + db + '.sqlite not found', 'red', attrs=['dark'])
        else:
            engine = create_engine('sqlite:///' + db + '.sqlite')
            Session = sessionmaker()
            Session.configure(bind=engine)
            session = Session()
            all_people = session.query(People).all()
            all_rooms = session.query(Rooms).all()

            found = False
            for person in all_people:
                for other_person in self.all_persons:
                    if other_person.person_name == person.person_name and other_person.person_surname == person.person_surname:
                        found = True
                if not found:
                    self.all_persons.append(person)

            for room in all_rooms:
                old_stdout = sys.stdout
                sys.stdout = StringIO()
                self.create_room(room.room_type, room.room_name)
                sys.stdout = old_stdout

                for person in room.room_persons.split(", "):
                    for each_person in self.all_persons:
                        if person and int(person) == each_person.iden:
                            for real_room in self.all_rooms:
                                if real_room.room_name == room.room_name and real_room.room_type == room.room_type:
                                    if each_person not in real_room.persons:
                                        real_room.persons.append(each_person)
                                        if real_room.room_type == "office":
                                            self.those_allocated_offices.append(each_person)
                                        elif real_room.room_type == "living_space":
                                            self.those_allocated_living_spaces.append(each_person)
            cprint("\n" + "Data loaded from " + db + ".sqlite successfully", 'green', attrs=['dark'])
