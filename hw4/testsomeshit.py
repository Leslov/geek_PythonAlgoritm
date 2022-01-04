# print(1 << 2 * 2)
# print(30 << 1)
# print(30 << 0)
xyu = '01'
c = f'0b{xyu*100}'
print(int(c, 2))

def foo(n):
    summ = 0
    for i in range(n):
        summ |= 1 << i * 2
    return summ
#print(foo(1))
#print(foo(2))
#print(foo(3))