num = int(input("Введите 3хзнчное целое число"))

num_1 = num // 100
num_2 = (num // 10) % 10
num_3 = num % 10

print(f" Сумма цифр в 3-х значном числе равна {num_1 + num_2 + num_3}")
print(f" Произведение цифр в 3-х значном числе равно {num_1 * num_2 * num_3}")