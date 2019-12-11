
def reverse(n):
    new = 0
    while n > 0:
        new = new * 10 + n % 10
        n = n // 10
    return new
n = int(input("Введите натуральное число n = "))
print(f'Исходное число N =  {n}\nОбратное число {reverse(n)}')