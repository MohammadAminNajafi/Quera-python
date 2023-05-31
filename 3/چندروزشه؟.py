from datetime import datetime

def day_s_born(x):
    birth_date = datetime.strptime(x, '%Y-%m-%d')
    today = datetime.strptime('1999-01-14', '%Y-%m-%d')
    days = (birth_date - today).days
    if days >= 0:
        return days
    else:
        return 'Not yet born'


print(day_s_born(input()))
