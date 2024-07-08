from datetime import datetime, timedelta

WEEKDAYS_LENGTH = 5
WEEK_LENGTH = 7


def get_upcoming_birthdays(users_list: list):
    date_format = '%Y.%m.%d'
    current_date = datetime.today().date()
    current_year = current_date.year
    users_for_congratulation = list()

    try:
        for user in users_list:
            user_birthday_date = datetime.strptime(user.get('birthday'), date_format).date()
            user_birthday_date_this_year = user_birthday_date.replace(year=current_year)
            delta = user_birthday_date_this_year - current_date

            if delta.days not in range(0, 7):
                continue

            updated_user_profile = {'name': user.get('name')}

            weekday = user_birthday_date_this_year.weekday()

            if weekday < WEEKDAYS_LENGTH:
                updated_user_profile.update({'congratulation_date': user_birthday_date_this_year.strftime(date_format)})
            else:
                congratulation_date = user_birthday_date_this_year + timedelta(days=WEEK_LENGTH - weekday)
                updated_user_profile.update({'congratulation_date': congratulation_date.strftime(date_format)})

            users_for_congratulation.append(updated_user_profile)

        return users_for_congratulation
    except Exception as e:
        print(e)


users = [
    {"name": "John Doe", "birthday": "1985.07.10"},
    {"name": "Jane Smith", "birthday": "1990.07.13"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)