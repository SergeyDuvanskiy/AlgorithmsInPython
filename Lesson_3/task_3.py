"""

В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

"""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный массив:\n {array}')

min_ = array[0]
max_ = array[0]
pos_min = 0
pos_max = 0

for idx, item in enumerate(array):
    if item < min_:
        min_ = item
        pos_min = idx
    elif item > max_:
        max_ = item
        pos_max = idx
print(f'min = {min_},\nmax = {max_}')

array[pos_min], array[pos_max] = array[pos_max], array[pos_min]

print(f' После замены min и max метсами : {array}')
