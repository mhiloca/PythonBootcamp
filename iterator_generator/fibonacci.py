def fib_gen(n):
    n1, n2 = 0, 1
    c = 0
    while c < n:
        n1, n2 = n2, n1 + n2
        yield n1
        c += 1


fib = fib_gen(10)
for i in range(10):
    print(next(fib), end=' | ')
