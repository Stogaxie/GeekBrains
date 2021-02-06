from functools import reduce

def my_func(prev_el, el):
    return prev_el * el
print(f'Четные значения: {[el for el in range(100, 1001) if el % 2 == 0]}')
print(f'Результат вычислений: {reduce(my_func, [el for el in range(100, 1001) if el % 2 == 0])}')
