def once(func):
    func.called = False

    def wrapper(*args):
        if func.called:
            return None
        func.called = True
        return func(*args)
    return wrapper


@once
def addition(a, b):
    return a + b


print(addition(3, 5))
print(addition(9, 7))
