from itertools import count

for el in count(int(input('Введите число: '))):
    print(el)
    if el > 500:
        break