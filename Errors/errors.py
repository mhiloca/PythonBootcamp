def colour(text, colour):
    colours = ('red', 'blue', 'yellow', 'green', 'pink', 'purple', 'orange')
    if colour not in colours:
        raise ValueError('invalid colour')
    if type(text) is not str:
        raise TypeError('text must be instance of str')
    if type(colour) is not str:
        raise TypeError('colour must be instance of str')
    return f'Printed {text} in {colour}'


def add(a, b):
    return a+b


# print(colour('Mhirley', 'magenta'))
# print(colour('Mhirley', 3))

add(1)
