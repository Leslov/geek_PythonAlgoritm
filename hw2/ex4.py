# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.
import helpers

n = helpers.input_by_type('Для подсчета суммы введите число элементов в ряде чисел 1, -0.5, 0.25, -0.125,…\n', int)
nth_elem = 1
summ = 0
for i in range(n):
    summ += nth_elem
    nth_elem /= -2
print(summ)