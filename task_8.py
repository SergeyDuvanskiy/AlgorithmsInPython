year = int(input("Ведите год в формате YYYY : "))

if year % 4 != 0:
    print(" Год обычный")
elif year % 100:
    if year % 400:
        print("Год высокосный")
    else:
        print("Год обычный")
else:
    print("Год высокосный")