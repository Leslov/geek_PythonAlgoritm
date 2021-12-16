# 3. Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
import random

import helpers


def get_two_values_from_user(type: callable, text, validator = None):
    x1 = helpers.input_by_type(f'{text} №1 ', type, validator)
    x2 = helpers.input_by_type(f'{text} №2 ', type, validator)
    return x1, x2


# a)
x1, x2 = get_two_values_from_user(int, 'Введите число')
arr = sorted((x1, x2))
a = random.randint(*arr)
print(f'a) Случайное целое число между введенных - {a}')

# b)
x1, x2 = get_two_values_from_user(int, 'Введите число')
arr = sorted((x1, x2))
b = random.uniform(*arr)
print(f'b) Случайное вещественное число между введенных - {b}')

# c)
onesymbol_validator = lambda x: x.isalpha() & len(x) == 1
x1, x2 = get_two_values_from_user(str, 'Введите букву', onesymbol_validator)
arr = sorted((x1, x2))
c = chr(random.randint(*[ord(x) for x in arr]))
print(f'c) Случайный символ: {c}')
