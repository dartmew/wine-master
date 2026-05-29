import datetime


def get_age():
    base_year = 1920
    now_year = datetime.datetime.now().year
    return now_year - base_year
