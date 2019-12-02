from random import choice


def soma(n, func):
    total = 0
    for num in range(n):
        total += func(num)
    return total


def square(n):
    return n * n


def greet(person):
    def get_mood():
        msg = choice(['Hi, there! ', 'I love you, ', 'Go away! '])
        return msg
    return get_mood() + person


print(greet('Mhiloca'))
