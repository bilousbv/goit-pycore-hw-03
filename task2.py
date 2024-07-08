import random

def get_numbers_ticket(min: int, max: int, quantity: int):
    try:
        if min < 1:
            raise Exception('Minimal number should be equal or more than 1')
        if max > 1000:
            raise Exception('Maximal number should be equal or less than 1000')
        if max < min:
            raise Exception('Maximal number should be more than minimal')
        if max - min < quantity:
            raise Exception('The quantity should be less than the difference between the maximum and minimum number')

        generated_numbers = set()

        while len(generated_numbers) < quantity:
            generated_numbers.add(random.randint(min, max))

        return list(generated_numbers)
    except Exception as e:
        print(e)


lottery_numbers = get_numbers_ticket(1, 49, 6)

if lottery_numbers is not None:
    print(f'Ваші лотерейні числа: {lottery_numbers}')
