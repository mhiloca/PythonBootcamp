from functools import wraps


def ensure_first_arg_is(n):
    def ensure(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if args and args[0] == n:
                print(fn(*args))
                return 'We are good'
            return 'Invalid arguments'
        return wrapper
    return ensure


@ensure_first_arg_is('burrito')
def concatena(x, y):
    return x + ' ' + y


@ensure_first_arg_is(10)
def soma(x, y):
    return x + y


print(concatena('burrito', 'good'))
print(soma(10, 8))