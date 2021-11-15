from enum import Enum

from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.data.db import Base


class Person(Base):
    __tablename__ = 'persons'

    persons_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    birthday = Column(Date, nullable=False)
    have_children = Column(Boolean)
    street_address = Column(String(120), nullable=False)
    zip_code = Column(String(15), nullable=False)
    city = Column(String(150), nullable=False)
    country = Column(String(45), nullable=False)
    phone_number = Column(String(45), nullable=False)
    email = Column(String(125))
    gender_id = Column(Integer, ForeignKey('gender.gender_id'))
    gender = relationship('Gender')


class Gender(Base):
    __tablename__ = 'gender'

    gender_id = Column(Integer, primary_key=True, autoincrement=True)
    gender_name = Column(String(25), nullable=False)


class GenderEnum(Enum):
    FEMALE = 1
    MALE = 2
    OTHER = 3