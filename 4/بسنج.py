import re


def validate_email(x):
    if re.match(r'^[a-zA-Z1-9\.\_]+@[a-zA-Z1-9]+\.[a-zA-Z]{3}$', x):
        return True
    else:
        return False


def validate_phone(y):
    if re.match(r'^09[0-9]{9}$', y) or re.match(r'^\+98[0-9]{10}$', y) or re.match(r'^00989[0-9]{9}$', y):
        return True
    else:
        return False

print(validate_phone('00981234567'))


