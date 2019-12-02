from random import randint


class Game:
    def __init__(self):
        self.mega = []
        while True:
            try:
                self.num = int(input('Number of games to simulate: '))
                break
            except ValueError:
                print('\033[31mInvalid value\033[m')

    def __repr__(self):
        return f'{self.num} lotery games generated'

    def _wager(self):
        self.mega = [randint(0, 60) if x not in self.mega else randint(0, 60) for x in range(6)]
        return self.mega

    def times(self):
        for i in range(self.num):
            print(self._wager())


class Decor:
    def __init__(self, lines):
        self.lines = lines
        print('- ' * lines)


Decor(20)
print(f'{"LOTERY SILMULATOR":^40}')
Decor(20)
tim = Game()
Decor(20)
tim.times()
Decor(20)
