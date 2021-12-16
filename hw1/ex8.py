# 8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
import sys

import helpers

while True:
    n1, n2, n3 = helpers.get_values_from_user('Введите число', 3, float)
    try:
        arr = sorted({n1, n2, n3})
        print(f'Среднее число: {arr[1]}')
        break
    except Exception:
        print('Введенные числа должны быть уникальными. Повторите ввод')
