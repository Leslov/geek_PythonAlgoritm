def get_simple1(N):
    # Не работает нихуя
    n = 'xyu'
    sieve = list(range(n + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(2*i, len(sieve), i):
                sieve[j] = 0
    simples = [x for x in sieve if x != 0]
    return simples[N]

print(get_simple1(100))