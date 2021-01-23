n = int(input("Введите число 'n':"))
print(f"Вы ввесли число {n}")

a = str(n)
double = a + a
triple = a + a + a
stack = n + int(double) + int(triple)

print(f"Сумма равна: {stack}")
