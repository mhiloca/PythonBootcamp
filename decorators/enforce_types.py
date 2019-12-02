from functools import wraps


def enforce(*types):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            new_args = []
            for (a, t) in zip(args, types):
                if type(a) != t:
                    new_args.append(t(a))
                else:
                    new_args.append(a)
            return fn(*new_args, **kwargs)
        return wrapper
    return inner


@enforce(str, str)
def concatena(x, y):
    return x + ' ' + y


print(concatena('hello', 89))
