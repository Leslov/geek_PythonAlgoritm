# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
import helpers

number = helpers.input_by_type('Введите число и я подсчитаю сумму четных/нечетных цифр\n', int)
length = len(str(number))
even_summ = 0
odd_summ = 0

for i in range(1, length):
    int_divisor = 10**i
    digit = number // int_divisor % 10
    if digit % 2 == 0:
        even_summ += digit
    else:
        odd_summ += digit

print(f'Сумма четных цифр: {even_summ}')
print(f'Сумма нечетных цифр: {odd_summ}')
