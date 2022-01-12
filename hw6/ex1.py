# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

# Сумма ряда чисел 1, -0.5, 0.25, -0.125,…
import sys


# from pympler import asizeof

def test_func(func):
    results = [
        1,
        0.5,
        0.75,
        0.625,
        0.6875,
        0.65625,
        0.671875,
        0.6640625,
        0.66796875,
        0.666015625
    ]
    for i in range(0, 10):
        f_val = func(i + 1)
        if f_val != results[i]:
            print(f'for i = {i}\t{f_val} != {results[i]}')
            assert False
    print(f"func '{func.__name__}' is OK")


def num_func_1(n):
    nth_elem = 1
    summ = 0
    for i in range(n):
        summ += nth_elem
        nth_elem /= -2
    memory_check(f'num_func_1({n})', nth_elem, summ)
    return summ


def num_func_2(n):
    def calc_top(num):
        summ = 0
        for i in range(num):
            summ |= 1 << i * 2
        return summ

    nm = n // 2  # число операций для поиска отрицательной суммы
    np = n - nm  # то же, для положительной суммы
    dif = np - nm
    mt = calc_top(nm)
    mb = 4 ** (nm - 1) * 2
    pt = mt + dif * (1 << (nm * 2))
    pb = 1 << ((np - 1) * 2)
    memory_check(f'num_func_2({n})', nm, np, dif, mt, mb, pt, pb)
    return pt / pb - mt / mb


def num_func_3(n):
    def calc_top(num):
        if num == 0:
            return 0
        c = f'0b{"01" * num}'  # Битовая маска
        return int(c, 2)  # На выходе получается для n = 1, 2, 3...: 1, 5, 21, 85...

    nm = n // 2  # число операций для поиска отрицательной суммы
    np = n - nm  # то же, для положительной суммы
    dif = np - nm
    mt = calc_top(nm)
    mb = 4 ** (nm - 1) * 2
    pt = mt + dif * (1 << (nm * 2))
    pb = 1 << ((np - 1) * 2)  # 4 ** (np - 1)
    memory_check(f'num_func_3({n})', nm, np, dif, mt, mb, pt, pb)
    return pt / pb - mt / mb


def test(func, rates):
    # test_func(func)

    for rate in rates:
        func(rate)
        # res = sys.getsizeof(1)#asizeof.asizeof(1)
        # res = timeit(lambda: func(rate), number=1000)
        # print(f'{func.__name__}({rate}): {res}')


def memory_check(func_name, *variables):
    memory_size = 0
    # print(variables)
    for var in variables:
        memory_size += sys.getsizeof(var)
    print(f'{func_name} uses {memory_size} bytes of memory')
    return memory_size


rates = [100, 1000, 10000, 100000, 1000000]
funcs = [num_func_1, num_func_2, num_func_3]
# for func in funcs:
#    test(func, rates)

test(num_func_1, rates)
test(num_func_2, rates)
test(num_func_3, rates)

# Детали:
# num_func_1:
# Объем занимаемой памяти:
# num_func_1(100)       uses 48 bytes of memory
# num_func_1(1000)      uses 48 bytes of memory
# num_func_1(10000)     uses 48 bytes of memory
# num_func_1(100000)    uses 48 bytes of memory
# Время выполнения:
# num_func_1(100):      0.004996
# num_func_1(1000):     0.051549
# num_func_1(10000):    0.531762
# num_func_1(100000):   5.206050
# Сложность линейная. Время выполнения на последней стадии (сек) t = n / 20000

# num_func_2:
# Объем занимаемой памяти:
# num_func_2(100)       uses 240 bytes of memory
# num_func_2(1000)      uses 720 bytes of memory
# num_func_2(10000)     uses 5520 bytes of memory
# num_func_2(100000)    uses 53520 bytes of memory
# Время выполнения:
# num_func_2(100):      0.004536
# num_func_2(1000):     0.045906
# num_func_2(10000):    3.244698
# num_func_2(100000):   113.765463
# Сложность нелинейная. Время выполнения на последней стадии (сек) t = n / 885

# num_func_3:
# Объем занимаемой памяти:
# num_func_3(100)       uses 240 bytes of memory
# num_func_3(1000)      uses 720 bytes of memory
# num_func_3(10000)     uses 5520 bytes of memory
# num_func_3(100000)    uses 53520 bytes of memory
# Время выполнения:
# num_func_3(100):      0.001436
# num_func_3(1000):     0.007611
# num_func_3(10000):    0.042845
# num_func_3(100000):   0.601078
# num_func_3(1000000):  7.018619
# Сложность почти линейная :). Время выполнения (сек) t = n / 142000

# Оптимальный алгоритм по объему занимаемой памяти - №1. Размер используемой памяти
# Оптимальный алгоритм по времени выполнения - №3. Его можно и дальше проапгрейдить.
# Нужно найти более оптимальный способ формирования битовой маски.
# Худший алгоритм - №2. Он и по памяти невыгоден и по времени выполнения
# Время выполнения растет в геометрической прогрессии. Объем занимаемой памяти растет линейно
