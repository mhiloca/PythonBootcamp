def divide(a, b):
    try:
        return int(a)/int(b)
    except ZeroDivisionError as err:
        return f'\033[31m{err}\033[m'
    except ValueError as err1:
        return f'\033[31m{err1}\033[m'


def get_key(d, key):
    try:
        return d[key]
    except KeyError:
        return None


# foobar
try:
    foobar
except:
    print('PROBLEM')

d = {'name': 'Mhirley', 'city': 'Florianópolis'}
print(get_key(d, 'name'))
"""
while True:
    try:
        num = int(input("please, enter a number: "))
    except:
        print("That's not a number")
    else:
        print("Good job, you've entered a number!")
        break
    finally:
        print("RUNS NO MATTER WHAT!")
print(f"You've entered {num}")
"""
n1 = input('Valor: ')
n2 = input('Valor: ')
print(divide(n1, n2))


