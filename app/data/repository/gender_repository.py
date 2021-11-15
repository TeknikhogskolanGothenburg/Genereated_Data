from app.data.db import session
from app.data.models import Gender


def create_gender(gender_name):
    gender = Gender(gender_name=gender_name)
    session.add(gender)
    session.commit()
