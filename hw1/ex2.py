import re
import helpers

def checkFormat(str):
    pattern = '^[0-9]+[.]?[0-9]*[,] [0-9]+[.]?[0-9]*$'
    regular = re.compile(pattern)
    return regular.match(str) != None

dot1 = helpers.input_by_type('Введите координаты 1 точки в формате "x, y"\n', str, checkFormat)
dot2 = helpers.input_by_type('Введите координаты 2 точки в формате "x, y"\n', str, checkFormat)
x1, y1 = [float(x) for x in dot1.split(", ")]
x2, y2 = [float(x) for x in dot2.split(", ")]

k = (y1 - y2) / (x1 - x2)
b = -(k*x1) + y1
result = f'y = {k}x + {b}'
print(result)