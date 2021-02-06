from random import randint

lst = []
for i in range(10):
    lst.append(randint(0, 999))
print(lst)
new_lst = [el for num, el in enumerate(lst) if lst[num - 1] < lst[num] ]
print(f'Полученный список: {new_lst}')
