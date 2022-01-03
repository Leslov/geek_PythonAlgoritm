# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

# Сумма ряда чисел 1, -0.5, 0.25, -0.125,…
from timeit import timeit


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
    return summ


def num_func_2(N):
    def calc_top(n):
        summ = 0
        for i in range(n):
            summ |= 1 << i * 2
        return summ

    nm = N // 2  # число операций для поиска отрицательной суммы
    np = N - nm  # то же, для положительной суммы
    dif = np - nm
    mt = calc_top(nm)
    mb = 4 ** (nm - 1) * 2
    pt = mt + dif * (1 << (nm*2))
    pb = 1 << ((np - 1)*2)
    return pt / pb - mt / mb


def num_func_3(N):
    def calc_top(n):
        if n == 0:
            return 0
        c = f'0b{"01" * n}' # Битовая маска
        return int(c, 2) # На выходе получается для n = 1, 2, 3...: 1, 5, 21, 85...

    nm = N // 2  # число операций для поиска отрицательной суммы
    np = N - nm  # то же, для положительной суммы
    dif = np - nm
    mt = calc_top(nm)
    mb = 4 ** (nm - 1) * 2
    pt = mt + dif * (1 << (nm*2))
    pb = 1 << ((np - 1)*2) # 4 ** (np - 1)

    return pt / pb - mt / mb

def test(func, rates):
    test_func(func)

    for rate in rates:
        res = timeit(lambda: func(rate), number=1000)
        print(f'{func.__name__}({rate}): {res:2f}')
rates = [100, 1000, 10000, 100000]
funcs = [num_func_1,num_func_2,num_func_3]
#for func in funcs:
#    test(func, rates)

test(num_func_3, [1000000])

# Детали: Время выполнения - примерное, актуально только для текущего состояния моего компа
# func 'num_func_1' is OK
# num_func_1(100):      0.004996
# num_func_1(1000):     0.051549
# num_func_1(10000):    0.531762
# num_func_1(100000):   5.206050
# Сложность линейная. Время выполнения на последней стадии (сек) t = n / 20000

# func 'num_func_2' is OK
# num_func_2(100):      0.004536
# num_func_2(1000):     0.045906
# num_func_2(10000):    3.244698
# num_func_2(100000):   113.765463
# Сложность нелинейная. Время выполнения на последней стадии (сек) t = n / 885

# func 'num_func_3' is OK
# num_func_3(100):      0.001436
# num_func_3(1000):     0.007611
# num_func_3(10000):    0.042845
# num_func_3(100000):   0.601078
# num_func_3(1000000):  7.018619
# Сложность почти линейная :). Время выполнения (сек) t = n / 142000

# Оптимальный алгоритм - №3. Его можно и дальше проапгрейдить.
# Нужно найти более оптимальный способ формирования битовой маски.
