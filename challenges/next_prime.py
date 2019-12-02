def next_primes():
    c = 2
    while True:
        if len([x for x in range(2, c+1) if c % x == 0]) == 1:
            yield c
        c += 1


primes = next_primes()
num = [next(primes) for y in range(10)]
print(num)