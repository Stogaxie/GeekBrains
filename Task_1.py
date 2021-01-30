def digit(*numbers):
    try:
        print("\n")
        number_1 = int(input("Введите делимое: "))
        number_2 = int(input("Введите делитель: "))
        result = (int(number_1 / number_2))
    except ValueError:
        return "Ошибка значения."
    except ZeroDivisionError:
        return "Ошибка! Деление на ноль."

    return result
print(f'Результат деления: {digit()}')
