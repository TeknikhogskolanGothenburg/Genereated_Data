import datetime

from app.controllers.person_controller import get_person_by_id, create_person
from app.data.db import session
from app.data.models import Person, GenderEnum
from app.data.models import GenderEnum

def main():
    person = {
        'first_name': 'Pelle',
        'last_name': 'Svensson',
        'birthday': datetime.date(1975, 3, 19),
        'have_children': True,
        'street_address': 'Småatan 64',
        'zip_code': '543 21',
        'city': 'Småstan',
        'country': 'Sweden',
        'phone_number': '+46 795 66 23',
        'email': 'per@email.com',
        'gender_id': GenderEnum.MALE
    }
    create_person(person)



if __name__ == '__main__':
    main()