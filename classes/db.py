from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class People(Base):

    __tablename__ = "people"

    iden = Column(Integer, primary_key=True)
    person_name = Column(String)
    person_surname = Column(String)
    person_type = Column(String)
    wants_accommodation = Column(String)

class Rooms(Base):

    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True)
    room_name = Column(String)
    room_type = Column(String)
    room_persons = Column(String)
