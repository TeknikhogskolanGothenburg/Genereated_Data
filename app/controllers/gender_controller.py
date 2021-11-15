from app.data.repository import gender_repository


def create_gender(gender_name):
    gender_repository.create_gender(gender_name)