a = int(input("Введите длинну первой стороны треугольника : "))
b = int(input("Введите длинну второй стороны треугольника : "))
c = int(input("Введите длинну третей стороны треугольника : "))

if a + b <= c or a + c <= b or b + c <= a:
    print(f' Треугольника с длинами сторон {a}, {b} и {c} не существует')
elif a != b and a != c and b != c:
    print(f' Треугольник с длинами сторон {a}, {b} и {c}  является разносторонним')
elif a == b == c:
    print(f' Треугольник с длинами сторон {a}, {b} и {c} является равносторонним')
else:
    print(f' Треугольник с длинами сторон {a}, {b} и {c} является равнобедренным')
