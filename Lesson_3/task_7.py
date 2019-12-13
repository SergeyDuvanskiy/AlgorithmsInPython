"""

В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться

"""
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)] #for testing, если одинаковые [2, 4, 5, 18, 3, 4, 2, 90, 9, 10]
print(f'Исходный массив:\n {array}')
if array[0] > array[1]:
    min_1 = 0
    min_2 = 1
else:
    min_1 = 1
    min_2 = 0

for i in range(2, SIZE):
    if array[i] < array[min_1]:
        spam_ = min_1
        min_1 = i
        if array[spam_] < array[min_2]:
            min_2 = spam_
    elif array[i] < array[min_2]:
        min_2 = i
print(f'Первый минимальный элемент: {array[min_1]}\nВторой минимальный элемент: {array[min_2]}')
