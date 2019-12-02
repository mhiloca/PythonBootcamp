def get_multiples(mul=1, maxim=10):
    c = 1
    while c <= maxim:
        yield c * mul
        c += 1


def get_unlimited_multiples(num):
    c = 1
    while True:
        yield c * num
        c += 1


multiples = (num for num in range(10))
print(next(multiples))