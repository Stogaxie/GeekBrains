list = [12, 4, 2, 2, 1, 0]
print(f"Текущий рейтинг - {list}")
print()
print("Для выхода введите: 00")
print()
number = int(input("Введите число: "))
if number == 00:
    print("Вы вышли из программы.")
while number != 00:
    for el in range(len(list)):
        if list[el] == number:
            list.insert(el + 1, number)
            break
        elif list[0] < number:
            list.insert(0, number)
        elif list[-1] > number:
            list.append(number)
        elif list[el] > number and list[el + 1] < number:
            list.insert(el + 1, number)
    print(f"Список обновлён - {list}")
    number = int(input("Введите число: "))
