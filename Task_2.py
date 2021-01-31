def info():
    name = input("Введите свое имя: ")
    lastname = input("Введите фамилию: ")
    year = (int(input("Введите год рождения: ")))
    city = input("Введите город проживания: ")
    email = input("Введите email: ")
    phone = input("Введите номер телефона: ")
    data = ([name,lastname, year, city, email, phone])
    return data
print(info())

