# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

import random
import timeit

def bubble_sort(arr):
    i = len(arr)
    while i > 0:
        for j in range(1, i):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
        i -= 1
    return arr


def bubble_sort_improved(arr):
    i = len(arr)
    while i > 0:
        is_fully_sorted = True
        for j in range(1, i):
            if arr[j - 1] > arr[j]:
                is_fully_sorted = False
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
        if is_fully_sorted:
            break
        i -= 1
    return arr

def test(*funcs):
    array = [random.randint(-100, 100) for _ in range(3000)]
    print(array)
    number = 10
    for func in funcs:
        print('*'*50)
        time = timeit.timeit(lambda: func(array), number=number)
        print(f'{func.__name__}: {time/number} seconds')
        print(func(array))

test(bubble_sort, bubble_sort_improved)

# bubble_sort: 0.24466999 seconds
# bubble_sort_improved: 0.0001489100000000132 seconds