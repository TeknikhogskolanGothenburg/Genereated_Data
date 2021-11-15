from app.data.repository import person_repository


def get_person_by_id(_id):
    return person_repository.get_person_by_id(_id)


def create_person(person):
    person_repository.create_person(person)
