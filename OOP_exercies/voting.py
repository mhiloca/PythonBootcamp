from functools import wraps


def decor(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('- ' * n)
            return func(*args, **kwargs)
        return wrapper
    return decorator


class Person:
    @decor(5)
    def __init__(self):
        first = input('First name: ').title().strip()
        last = input('Surname: ').title().strip()
        self.name = first+' '+last
        while True:
            try:
                age = int(input('Age: '))
                if 0 > age > 130:
                    print('\033[31mInvalid age\033[m')
                else:
                    self.age = age
                    break
            except ValueError:
                print('\033[31mInvalid value\033[m')

    def __repr__(self):
        return f'{self.name} - {self.age} years old'


class Voting(Person):

    def __init__(self):
        super().__init__()
        self.status = self._vote()

    def _vote(self):
        if self.age < 16:
            return 'NOT ALLOWED'
        return 'ALLOWED'

    @decor(10)
    def __repr__(self):
        return f'{self.name}, {self.age} years old - {self.status} voting'


person1 = Voting()
print(person1)
