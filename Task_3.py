def func(n1, n2, n3):
    if n1 >= n3 and n2 >= n3:
        return n1 + n2
    elif n1 > n2 and n1 < n3:
        return n1 + n3
    else:
        return n2 + n3
print(f'Результат равен: {func(int(input("Введите первое число: ")), int(input("Введите второе число: ")), int(input("Введите третье число: ")))}')
