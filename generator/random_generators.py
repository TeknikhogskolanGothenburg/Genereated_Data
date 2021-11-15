import datetime
import json
import random

from app.controllers.person_controller import create_person
from app.data.models import GenderEnum

female_first = [line.strip() for line in open('data_files/female_first.txt', 'r', encoding='utf-8')]
male_first = [line.strip() for line in open('data_files/male_first.txt', 'r', encoding='utf-8')]
last_names = [line.strip() for line in open('data_files/lastnames.txt', 'r', encoding='utf-8')]
phone_numbers = [line.strip() for line in open('data_files/20k_swedish_phonenumbers.txt', 'r', encoding='utf-8')]

with open('data_files/postcodes.json', 'r', encoding='utf-8') as postcode_file:
    postcodes = json.load(postcode_file)
    postcodes_list = []
    for postcode_list in postcodes.values():
        for postcode_dict in postcode_list:
            postcodes_list.append(postcode_dict)


def random_female_name():
    return random.choice(female_first)


def random_male_name():
    return random.choice(male_first)


def random_last_name():
    return random.choice(last_names)


def random_address():
    return random.choice(postcodes_list)


def random_phone_number():
    return random.choice(phone_numbers)


def random_birthday(start_date, end_date):
    """
    Generates a random date between start_date and end_date
    :param start_date: str in format YYYY-mm-dd
    :param end_date: str in format YYYY-mm-dd
    :return: datetime.date()
    """
    # Checking the data
    if len(start_date.split('-')) != 3 or len(end_date.split('-')) != 3:
        raise ValueError("Dates must be a str given in the format YYYY-mm-dd")

    start_year, start_month, start_day = start_date.split('-')
    end_year, end_month, end_day = end_date.split('-')
    for d in [start_year, start_month, start_day, end_year, end_month, end_day]:
        if not d.isdigit():
            raise ValueError("Dates must be a str given in the format YYYY-mm-dd")

    start_date = datetime.date(int(start_year), int(start_month), int(start_day))
    end_date = datetime.date(int(end_year), int(end_month), int(end_day))

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    return start_date + datetime.timedelta(days=random_number_of_days)


def generate_random_email(first_name, last_name):
    email_hosts = ['gmail.com', 'hotmail.com', 'outlook.com', 'live.se', 'yahoo.com']
    return f'{first_name.lower()}.{last_name.lower()}@{random.choice(email_hosts)}'


def generate_random_person(gender):
    if gender.lower() == 'female':
        first_name = random_female_name()
        gender = GenderEnum.FEMALE
    elif gender.lower() == 'male':
        first_name = random_male_name()
        gender = GenderEnum.MALE
    else:
        first_name = random.choice(female_first + male_first)
        gender = GenderEnum.OTHER

    last_name = random_last_name()

    address = random_address()
    if 'Street/Box No.' not in address:
        street_no = ''
    else:
        street_no = address['Street/Box No.']
        if len(street_no) != 0:
            if len(street_no.split(' - ')) != 2:
                street_no = '1'
            else:
                start_no, end_no = street_no.split(' - ')
                street_no = str(random.choice(list(range(int(start_no), int(end_no) + 1))))

    address['Street Name'] += ' ' + street_no

    phone_number = random_phone_number()
    email = generate_random_email(first_name, last_name)
    birthday = random_birthday('1929-01-01', '2002-12-31')
    have_children = random.choice([True, False, None])

    return {
        'first_name': first_name,
        'last_name': last_name,
        'birthday': birthday,
        'have_children': have_children,
        'street_address': address['Street Name'],
        'zip_code': address['Postcode'],
        'city': address['City/Locality'],
        'country': 'Sweden',
        'phone_number': phone_number,
        'email': email,
        'gender_id': gender
    }


def main():
    for _ in range(10_000_000):
        gender_no = random.randrange(1, 101)
        if gender_no == 1:
            person = generate_random_person('other')
        elif 1 < gender_no < 51:
            person = generate_random_person('female')
        else:
            person = generate_random_person('male')

        create_person(person)



if __name__ == '__main__':
    main()