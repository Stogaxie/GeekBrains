def sum ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Введите число: ').split()
        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Текущая сумма равна:  {sum_res}')
    print(f'Финальная сумма равна:  {sum_res}')
sum()
