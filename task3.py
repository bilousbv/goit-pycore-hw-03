import re

CORRECT_PHONE_NUMBER_LENGTH = 13


def normalize_phone(phone_number: str):
    try:
        pattern = r'(\+*38)*(\D)*'
        pure_phone_number = re.sub(pattern, '', phone_number)
        formatted_phone_number = f'+38{pure_phone_number}'

        if len(formatted_phone_number) is not CORRECT_PHONE_NUMBER_LENGTH:
            raise Exception('Phone number is invalid')

        return formatted_phone_number
    except Exception as e:
        print(e)


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)