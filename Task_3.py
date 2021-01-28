month = int(input('Введите номер месяца: '))
seasons = {'зима': (12, 1, 2),
           'весна': (3, 4, 5),
           'лето': (6, 7, 8),
           'осень': (9, 10, 11)
           }
for key in seasons.keys():
    if month in seasons[key]:
        print(f'{month} месяц - {key}!')
