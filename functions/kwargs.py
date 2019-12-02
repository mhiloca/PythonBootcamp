def special_greeting(**kwargs):
    name = *kwargs,
    if 'Mhirley' in kwargs and kwargs['Mhirley'] == 'special':
        return f'{name[0]}, here is your special greeting!'
    elif 'Mhirley' in kwargs:
        return f'{kwargs["Mhirley"]}, {name[0]}!'
    return 'Not sure who you are...'


def sum_all_values(*args):
    print(args)
    total = 0
    for n in args:
        total += n
    return total


def display_names(**kwargs):
    keys = *kwargs,
    return f'{kwargs[keys[0]]} says hello to {kwargs[keys[1]]}'


print(special_greeting(Gustavo='special'))
print(special_greeting(Mhirley='special'))
print(special_greeting(Mhirley='Hello'))

nums = 1, 2, 3, 4, 5, 6
print(sum_all_values(*nums))

names = {'firt': 'Mhirley', 'second': 'Gustavo'}
print(display_names(**names))

