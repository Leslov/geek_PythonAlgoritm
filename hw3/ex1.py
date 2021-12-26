print('1. В диапазоне натуральных чисел от 2 до 99 определить,')
print('сколько из них кратны каждому из чисел в диапазоне от 2 до 9. Примечание: 8 разных ответов.')

result = {x: 0 for x in range(2, 10)}
for key in result.keys():
    for x in range(2,100):
        if x % key == 0:
            result[key] += 1



for key, value in result.items():
    print(f'Числу {key} кратны {value} значений массива 2-99')
