str1 = input("Введите строку: ")
lst = []
number = 1
for el in range(str1.count(' ') + 1):
    lst = str1.split()
    if len(str(lst)) <= 10:
        print(f"{number} {lst [el]}")
        number += 1
    else:
        print(f"{number} {lst [el] [0:10]}")
        number += 1