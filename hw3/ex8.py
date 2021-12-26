from random import randint
import helpers
print('8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.\n'
      'Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.\n'
      'В конце следует вывести полученную матрицу.')
matrix = []
hor_len = 4
ver_len = 4
print('Заполните матрицу значениями')
for _ in range(ver_len):
    # Если ты хочешь проверить и лень вводить с руки 16 значений, то раскоментируй строчку ниже:
    #line = [randint(1, 10) for x in range(hor_len)]
    line = [helpers.input_by_type('', int) for x in range(hor_len)] #и закоментируй меня. #StudentsLifeMatter
    matrix.append(line)

# генерим ласт строчку (сумма по вертикали)
last_line = []
for col in range(ver_len):
    ver_line = [matrix[i][col] for i in range(hor_len)]
    sum = 0
    for x in ver_line:
        sum += x
    last_line.append(sum)
matrix.append(last_line)
for line in matrix:
    print(line)