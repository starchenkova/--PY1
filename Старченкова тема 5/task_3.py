
from random import randint
def get_unique_list_numbers():
    list_unique_numbers = []
    while len(list_unique_numbers) <= 15:
        number = randint(-10, 10)
        if number in list_unique_numbers:
            pass
        else:
            list_unique_numbers.append(number)
    return list_unique_numbers

list_ = get_unique_list_numbers()
print(list_)
