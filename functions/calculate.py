def calculate(**kwargs):
    total = 0
    n1 = kwargs['first']
    n2 = kwargs['second']
    if kwargs['operation'] == 'add':
        total = n1 + n2
    elif kwargs['operation'] == 'subtract':
        total = n1 - n2
    elif kwargs['operation'] == 'multiply':
        total = n1 * n2
    elif kwargs['operation'] == 'divide':
        total = n1 / n2
    if kwargs['make_float']:
        total = f'{total:.1f}'
    else:
        total = int(total)
    if 'message' in kwargs:
        return f'{kwargs["message"]} {total}'
    return f'The result is {total}'


data = dict(make_float=True, first=24, second=2, operation='divide', message='You just divided')
print(calculate(**data))


