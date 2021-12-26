from random import randint


def switch_min_max(arr):
    min = 9999
    max = 0
    for i, x in enumerate(arr):
        if x < min:
            min = x
            min_i = i
        if x > max:
            max = x
            max_i = i
    arr[min_i] = max
    arr[max_i] = min
    return arr


print('3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.')
arr = [randint(1, 20) for x in range(10)]
print(f'Исходный массив:   {arr}')
arr = switch_min_max(arr)
print(f'Полученный массив: {arr}')
