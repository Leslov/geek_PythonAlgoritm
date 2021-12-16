# 4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
import helpers


def get_two_values_from_user(type: callable, text, validator=None):
    x1 = helpers.input_by_type(f'{text} №1 ', type, validator)
    x2 = helpers.input_by_type(f'{text} №2 ', type, validator)
    return x1, x2


onesymbol_validator = lambda x: x.isalpha() & len(x) == 1
ch1, ch2 = get_two_values_from_user(str, 'Введите букву', onesymbol_validator)
a_ind = ord('a')
ch1_ind = ord(ch1) - a_ind
ch2_ind = ord(ch2) - a_ind

print(f'Позиция буквы {ch1} в алфавите: {ch1_ind + 1}')
print(f'Позиция буквы {ch2} в алфавите: {ch2_ind + 1}')
print(f'Расстояние между ними: {abs(ch1_ind - ch2_ind)}')
