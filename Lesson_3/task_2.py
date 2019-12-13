"""

Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля), т.к. именно
в этих позициях первого массива стоят четные числа.

"""
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
list_numbers = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)] #[_ for _ in range(10)] - for testing
print(f'Исходный массив:\n {list_numbers}')

new_list = []

for idx, item in enumerate(list_numbers):
    if item % 2 == 0:
        new_list.append(idx)
print(f'Итоговый массив , элементами которого являются позиции четных элементов иходного массива:\n {new_list}')
