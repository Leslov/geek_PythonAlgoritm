# 7. Определить, является ли год, который ввел пользователь, високосным или не високосным.
import helpers

year = helpers.input_by_type('Введите год и я скажу, високосный ли он', int)
if year % 4 == 0:
    result = 'Год високосный'
else:
    result = 'Год не високосный'
print(result)
