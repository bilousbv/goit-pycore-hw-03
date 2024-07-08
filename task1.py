import re
from datetime import datetime


def get_days_from_today(date: str):
    try:
        date_format = '%Y-%m-%d'
        entered_date = datetime.strptime(date, date_format)
        current_date = datetime.today()
        delta = current_date - entered_date
        return delta.days

    except ValueError:
        print('Please enter the valid date using following format YYYY-MM-DD')


days_difference = get_days_from_today('07-06-2024')

if days_difference is not None:
    print(days_difference)
