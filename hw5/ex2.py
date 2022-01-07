import collections
import math

print('2. Написать программу сложения и умножения двух шестнадцатеричных чисел.\n'
      'При этом каждое число представляется как массив, элементы которого — цифры числа.\n'
      'Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.\n'
      'Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].\n'
      'Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления,\n'
      'задача решается в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит.\n'
      'Поэтому использование встроенных функций для перевода\n'
      'из одной системы счисления в другую в данной задаче под запретом.')

hexes = tuple(range(ord('0'), ord('9') + 1)) + tuple(range(ord('A'), ord('F') + 1))
d_hexes = collections.OrderedDict({hexes[i]: i for i in range(len(hexes))})  # key - 56, value - 10


def convert(num):  # Конвертирует строчную запись шестнадцатетиричной цифры в 10-ричную систему (int)
    def convert_single_num(number):
        if len(number) != 1:
            raise AttributeError(f'"{num}" не является шестнадцетиричной цифрой. Длина не равна единице.')
        val = ord(number)
        if d_hexes.__contains__(val) == False:
            raise AttributeError(f'"{number}" не является шестнадцетиричной цифрой')
        return d_hexes[val]

    result = 0
    for i in range(len(num)):
        result += (convert_single_num(num[-i - 1]) & 15) << (i * 4)
    return result


def convertback(n):  # Конвертирует int в строчную запись шестнадцатетиричной цифры
    def to16(integer):  # Конвертация инта в 16-ричную цифру (0-F). Падает, если подать значение вне диапазона 0-15
        return chr(next(key for key, value in d_hexes.items() if value == integer))

    if n == 0:
        return '0'
    letters = ''
    for i in range(0, bits_count(n), 4):
        val = (n >> i) & 15
        letters += to16(val)
    return letters[::-1]


def bits_count(num):
    if num == 0:
        return 0
    return math.floor(math.log2(num)) + 1


def get_bits(number):
    count = bits_count(number)
    bits = [None] * count
    for i in range(count):
        bits[i] = number >> i & 1
    return bits


def increment(num1, num2):
    num1, num2 = convert(num1), convert(num2)
    result = 0
    for i in range(bits_count(max([num1, num2]))):
        andbit = 1 << i
        result += (num1 & andbit) + (num2 & andbit)
    return convertback(result)


def multiply(num1, num2):
    num1, num2 = convert(num1), convert(num2)
    num2_bits = get_bits(num2)
    result = 0
    for i in range(len(num2_bits)):
        result += (((num2 >> i) & 1) * num1) << i
    return convertback(result)


def test():
    if convertback(16) != '10' or convertback(4594) != '11F2':
        raise SystemError('convertback fails')
    if convert('10') != 16 or convert('11F2') != 4594:
        raise SystemError('convert fails')
    if bits_count(15) != 4 or bits_count(16) != 5 or bits_count(1) != 1:
        raise SystemError('bits_count fails')
    if get_bits(15) != [1, 1, 1, 1] or get_bits(16) != [0, 0, 0, 0, 1]:
        raise SystemError('get_bits fails')
    if increment('5', '8') != 'D' or increment('12', 'AA') != 'BC' or increment('1', 'AA') != 'AB':
        raise SystemError('increment fails')
    if multiply('5', '8') != '28' or multiply('12', 'AA') != 'BF4' or multiply('1', 'AA') != 'AA':
        raise SystemError('multiply fails')
    print('All tests is OK')


test()
while True:
    print('*' * 50)
    print('Оставьте ввод пустым, чтобы завершить программу')
    n1 = input('Первое число: ')
    if not n1:
        break
    n2 = input('Второе число: ')
    operation = input('Введите выполняемую операцию (+ или *)')
    oper = None
    if operation == '+':
        oper = increment
    elif operation == '*':
        oper = multiply
    else:
        print('Тип опреации не распознан. Повторите ввод')
        continue
    print(f'{n1} {operation} {n2} = {oper(n1, n2)}')
