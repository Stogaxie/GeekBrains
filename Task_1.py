def profit():
    try:
        worktime = float(input('Отработанное время (в часах): '))
        salary = int(input('Ставка работника (за час):  '))
        bonus = int(input('Премия:  '))
        result = worktime * salary + bonus
        print(f'Заработная плата сотрудника:   {result}')
    except ValueError:
       return print('Ошибка!')
profit()