from random import random
n = round(random() * 100)
count = 1
print("Загадано случайное число от 0 до 100, у Вас 10 попыток, чтобы отгадать")

while count <= 10:
    guess = int(input(str(count)+" ая попытка, введите число"))
    if guess > n:
        print("Много")
        count += 1
    elif guess < n:
        print("Мало")
        count += 1
    else:
        print(f" Вы угадали с {count} попытки! Поздравляем")
        break
else:
    print("Вы использовали все 10 попыток")
