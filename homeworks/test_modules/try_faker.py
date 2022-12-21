from faker import Faker
from collections import defaultdict

fake = Faker()


def check_password(password):
    len_pass = len(password)
    dict_count_char = defaultdict(int)
    for char in password:
        if char.isalpha():
            dict_count_char['letter'] += 1
        elif char.isdigit():
            dict_count_char['number'] += 1
    if dict_count_char['number'] < 1:
        error = 'Not valid password: must contain at least one non-alphabetic character'
    elif len_pass < 8:
        error = 'Not valid password: must contain at least 8 characters'
    elif password != str(set(password)) and len_pass > len(set(password)) + 1:
        error = 'Not valid: contains more than two repeated characters'
    elif dict_count_char['letter'] < 4:
        error = 'Not valid password: must contain at least four alphabetic characters'
    else:
        error = 'Valid password'
    return error


def create_user(name: str, password: str):
    if not name:
        name = fake.name()
    if not password:
        password = fake.password()
    print(f'user name is "{name}", password "{password}"')
    print(check_password(password))
    return name, password
