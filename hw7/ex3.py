# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
import timeit
from random import randint, random, shuffle

m = randint(1000, 3000)
# array = [random() for _ in range(2*m+1)]
array = [x for x in range(2 * m + 1)]
shuffle(array)


def get_mediane_1(arr):
    for num in arr:
        l_count, h_count = 0, 0
        for i in range(len(arr)):
            if arr[i] > num:
                h_count += 1
            elif arr[i] < num:
                l_count += 1
        # Допустим, медиана всегда делит массив на две равные части. Т.е. числа не повторяются
        if l_count == h_count:
            return num


def get_mediane_2(arr):
    skip_ids = {}  # Срезаем часть массива, чтобы не выполнять лишние вычисления
    for i in range(len(arr)):
        if i in skip_ids:
            continue
        num = arr[i]
        l, h = [], []
        for j in range(len(arr)):
            if arr[j] > num:
                h.append(j)
            elif arr[j] < num:
                l.append(j)
        # Допустим, медиана всегда делит массив на две равные части. Т.е. числа не повторяются
        l_count, h_count = len(l), len(h)
        if l_count == h_count:
            return num
        elif l_count > h_count:
            skip_ids = set(list(skip_ids) + h)
        elif l_count < h_count:
            skip_ids = set(list(skip_ids) + l)


def test_func(func):
    mediane = func([x for x in range(2 * 10 + 1)])
    assert mediane == 10
    print(f'{func.__name__}: {timeit.timeit(lambda: func(array), number=10)}')


print(array)
# test_func(get_mediane_1)
test_func(get_mediane_2)

mediane = get_mediane_2(array)
print(f'Медиана массива: {mediane}')

# При малом размере массива скорость слабо различается. При большом размере - второй алгоритм выходит гораздо быстрее.
# Чем больше размер, тем заметней разница
