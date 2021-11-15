from app.data.db import session
from app.data.models import Person


def get_person_by_id(_id):
    return session.query(Person).filter(Person.persons_id == _id).first()


def create_person(person):
    person['gender_id'] = person['gender_id'].value
    person = Person(**person)
    session.add(person)
    session.commit()