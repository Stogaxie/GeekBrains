with open('salary.txt', 'r') as my_file:
    sal = []
    cash = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           cash.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20000 {cash}, средний оклад {sum(map(int, sal)) / len(sal)}')
