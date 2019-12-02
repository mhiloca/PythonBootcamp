from time import time


def speed_test(fn):
    def wrapper(*args, **kwargs):
        start = time()
        fn(*args, **kwargs)
        total = time() - start
        return f'It took {total}sec to execute the function'
    return wrapper


@speed_test
def soma(*args):
    return sum(*args)


print(soma([x for x in range(100000)]))
print('- ' * 15)
print(soma(x for x in range(100000)))
