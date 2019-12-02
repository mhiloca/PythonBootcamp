def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper

@shout
def greet(name):
    return f'Hi, my name is {name}'

@shout
def order(main, side):
    return f'Hi, I\'d like to order {main} with {side} on the side'


greet_mhi = greet('Mhirley')
order_rice_beans = order('beans', 'rice')

print(greet_mhi)
print(order_rice_beans)