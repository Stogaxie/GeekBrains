print("Введите ваши данные:")

name = input("Введите имя:")
lastname = input("Введите фамилию:")
age = int(input("Введите возраст (лет):"))
print(name,lastname,age)
a = name
b = lastname
c = age

if c < 18:
    print('Доступ запрещён!')
else:
    s = f'Меня зовут {a} {b}, мне {c} лет!'
    print(s)