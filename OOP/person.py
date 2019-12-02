class Person:
    def __init__(self, name):
        self.name = name
        self._secret = 'Hi!'
        self.__msg = 'I like turtles'

    def doorman(self, guess):
        if guess == self._secret:
            print('You may come in')
        else:
            print('Get out!')


d = Person('Mike')
d.doorman('Hi!')
