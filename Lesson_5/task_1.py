"""

Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
чья прибыль выше среднего и ниже среднего.

"""
from collections import namedtuple

Factory = namedtuple('Factory', 'name, income_q1, income_q2, income_q3, income_q4')
n = int(input("Введите количество предприятий"))
new_factory = []  # массив в котором храню namedtuple объекты каждой компании
income_sum = []   # массив, в котором храню доход каждой компании за 4 квартала
common_sum = 0    # Общая сумма дохода всех компаний
for i in range(n):
    print(f'Введите информацию о  {i+1} фабрике :')
    name = input('Введите имя компании')
    income_q1 = float(input('Введите доход за Q1'))
    income_q2 = float(input('Введите доход за Q2'))
    income_q3 = float(input('Введите доход за Q3'))
    income_q4 = float(input('Введите доход за Q4'))
    new_factory.append(Factory(name, income_q1, income_q2, income_q3, income_q4))
    income_sum.append(income_q1 + income_q2 + income_q3 + income_q4)
    common_sum += income_sum[i]
average = common_sum / n
print(f'Средний доход за год всех {n} предприятий : {average}')
for i in range(n):
    if income_sum[i] < average:
        print(f'Предприятие {new_factory[i].name} имеет прибыль {income_sum[i]} меньше среднего {average}')
    elif income_sum[i] > average:
        print(f'Предприятие{new_factory[i].name} имеет прибыль {income_sum[i]} выше среднего {average}')
    else:
        print(f'Предприятие{new_factory[i].name} имеет прибыль {income_sum[i]} равную среднему {average}')


