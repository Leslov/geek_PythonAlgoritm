# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
from random import randint

array = [randint(0, 50) for _ in range(25)]


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    half_len = len(arr) // 2
    left, right = arr[:half_len], arr[half_len:]
    result = [None] * (len(left) + len(right))
    merge_sort(left)
    merge_sort(right)
    left_index = right_index = result_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result[result_index] = left[left_index]
            left_index += 1
        else:
            result[result_index] = right[right_index]
            right_index += 1
        result_index += 1
    while left_index < len(left):
        result[result_index] = left[left_index]
        left_index += 1
        result_index += 1
    while right_index < len(right):
        result[result_index] = right[right_index]
        right_index += 1
        result_index += 1
    for i in range(len(arr)):
        arr[i] = result[i]
    return arr


print(array)
print(merge_sort(array))
