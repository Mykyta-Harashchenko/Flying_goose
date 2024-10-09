import random

def get_numbers_ticket(min, max ,quantity :int):
    numbers = random.sample(range(min, max+1), k = quantity)
    return numbers

lottery_numbers = get_numbers_ticket(1, 49, 6)
print('Ваші лотерейні числа:', lottery_numbers)