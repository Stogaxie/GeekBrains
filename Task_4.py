n = int(input("Введите целое положительное число: "))
x = 0
while n > 0:
    y = n % 10
    if y > x:
        x = y
    n = n//10
print("Результат:", x)