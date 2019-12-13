"""
В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9

"""

MIN_ITEM = 2
MAX_ITEM = 100
array = [0] * 8
for i in range(MIN_ITEM, MAX_ITEM):
    count = 0
    for j in range(2, 10):
        if i % j == 0:
            array[j - 2] += 1

item = 0
while item < len(array):
    print(f'Количество чисел кратных {item + 2} - {array[item]} ')
    item += 1
