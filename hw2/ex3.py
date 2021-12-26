# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.
import helpers

result = 0
number = helpers.input_by_type('Введите число и я его разверну', int)
length = len(str(number))
for i in range(1, length + 1):
    multiplier = 10**(length - i)
    int_divisor = 10**(i - 1)
    result += number // int_divisor % 10 * multiplier
print(result)
