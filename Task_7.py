import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('firm.txt', 'r') as file:
    for line in file:
        name, liability, earn, lose = line.split()
        profit[name] = int(earn) - int(lose)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Усредненная прибыль: {prof_aver:.2f}')
    else:
        print(f'Компании отработали в убыток.')
    pr = {'Усредненная прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании: {profit}')

with open('firm.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'Создан файл json: \n '
          f' {js_str}')
