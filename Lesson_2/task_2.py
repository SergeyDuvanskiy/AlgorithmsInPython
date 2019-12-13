n = int(input("ВВедите натуральное число n = "))
even_count = odd_count = 0
while n > 0:
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    n = n // 10
print(f'Четных цифр в числе N - {even_count}\nНечетных - {odd_count}')
