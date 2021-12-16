# 5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
import helpers

ch_ind = helpers.input_by_type('Введите индекс буквы', int, lambda x: 1 <= x <= 26)
a_ind = ord('a')
ch = chr(ch_ind + a_ind - 1)
print(f'Буква под номером {ch_ind} это {ch}')
