from functools import wraps


def ensure_fewer_than_three_args(fn):
    @wraps(fn)
    def wrapper(*args):
        if len(args) > 2:
            raise ValueError('Too many arguments!')
        return fn(*args)
    return wrapper


def only_ints(fn):
    @wraps(fn)
    def wrapper(*args):
        if any([arg for arg in args if type(arg) != int]):
            return 'Please only invoke integers'
        print(f'Calling {fn.__name__}')
        return fn(*args)
    return wrapper


@only_ints
def soma(x, y):
    return x + y


print(soma(9, 2))