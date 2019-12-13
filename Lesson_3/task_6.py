"""

В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать

"""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [11, 99, 74, 100, 27, 80, 7, 84, 50, 100]#[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
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

sum_ = 0
for idx, item in enumerate(array):
    if pos_min < idx < pos_max:
        print(item)
        sum_ += item
    elif pos_max < idx < pos_min:
        print(item)
        sum_ += item
print(f' Сумма элементов между минимальным и максимальным равна :  {sum_}')
