def calculate(**kwargs):
    n1 = kwargs.get('first', 0)
    n2 = kwargs.get('second', 0)
    operation_lookup = {
        'add': n1 + n2,
        'subtract': n1 - n2,
        'multiply': n1 * n2,
        'divide': n1 / n2
    }
    is_float = kwargs.get('make_float', False)
    total = operation_lookup[kwargs.get('operation', ' ')]
    if is_float:
        total = f'{total:.1f}'
    else:
        total = int(total)
    return f'{kwargs.get("message", "The result is")} {total}'


data = dict(first=12, second=3, operation='divide', message='You just divided')
print(calculate(**data))
