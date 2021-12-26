from random import randint

print('4. Определить, какое число в массиве встречается чаще всего.')
arr = [randint(1, 10) for x in range(20)]
result = {x: 0 for x in set(arr)}
for x in arr:
    result[x] += 1

max = -1
for key, value in result.items():
    if value > max:
        max_i, max = key, value

print(result)
print(f'Число {max_i} встречается {max} раз')
