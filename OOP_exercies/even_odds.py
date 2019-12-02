from random import randint, choice
from time import sleep


def decor(n):
    print('- ' * n)


class Player:
    def __init__(self):
        self.name = input('Player name: ').title()
        if self.name[:3] == 'Com':
            self.name = 'Computer'

    def __repr__(self):
        return f'Player {self.name}'


class OddsEvens:

    ans_pl1 = ans_pl2 = ''
    num_pl1 = num_pl2 = 0

    def __init__(self, pl1, pl2):
        self.pl1 = pl1
        self.pl2 = pl2

    def __repr__(self):
        sleep(1)
        return f'{self.pl1} X {self.pl2}'

    def _odds_evens(self):
        decor(5)
        sleep(1)
        pl = randint(0, 1)
        if pl:
            player = self.pl2
            print(f'{self.pl2} chooses')
        else:
            player = self.pl1
            print(f'{self.pl1} chooses')
        answers = ['EVENS', 'ODDS']
        if player == self.pl1:
            while True:
                OddsEvens.ans_pl1 = input('Your choice: ').upper().strip()
                if OddsEvens.ans_pl1 in answers:
                    answers.remove(OddsEvens.ans_pl1)
                    OddsEvens.ans_pl2 = answers[0]
                    break
                else:
                    print('\033[31mInvalid answer\033[m')
        else:
            if self.pl2.name == 'Computer':
                OddsEvens.ans_pl2 = choice(answers)
                answers.remove(OddsEvens.ans_pl2)
                OddsEvens.ans_pl1 = answers[0]
            else:
                while True:
                    OddsEvens.ans_pl2 = input('Your choice: ').upper().strip()
                    if OddsEvens.ans_pl2 in answers:
                        answers.remove(OddsEvens.ans_pl2)
                        OddsEvens.ans_pl1 = answers[0]
                        break
                    else:
                        print('\033[31mInvalid answer\33[m')
        sleep(1)
        return f'{self.pl1} is {OddsEvens.ans_pl1} and {self.pl2} is {OddsEvens.ans_pl2}'

    def play(self):
        print(self._odds_evens())
        decor(10)
        while True:
            try:
                OddsEvens.num_pl1 = int(input(f'{self.pl1.name} - Number from 0 to 10: '))
                if 0 > OddsEvens.num_pl1 > 10:
                    print('\033[31mInvalid number\033[m')
                else:
                    break
            except ValueError:
                print('\033[31mInvalid number\033[m')
        if self.pl2.name == 'Computer':
            OddsEvens.num_pl2 = randint(0, 10)
        else:
            while True:
                try:
                    OddsEvens.num_pl2 = int(input(f'{self.pl2.name} - Number from 0 to 10: '))
                    if 0 > OddsEvens.num_pl2 > 10:
                        print('\033[31mInvalid number\033[m')
                    else:
                        break
                except ValueError:
                    print('\033[31mInvalid number\033[m')
        decor(10)
        return f'{self.pl1.name} plays {OddsEvens.num_pl1} - {self.pl2.name} plays {OddsEvens.num_pl2}'

    def results(self):
        res = OddsEvens.num_pl1 + OddsEvens.num_pl2
        if res % 2 == 0:
            win = 'EVENS'
        else:
            win = 'ODDS'
        if OddsEvens.ans_pl1 == win:
            winner = self.pl1
        else:
            winner = self.pl2
        return f'{res} is {win} - {winner} wins!'


decor(15)
print('Let\'s play Evens and Odds!\n'
      'Enter your name and the name of your opponent\n'
      'ENTER "computer" if playing against me!')
decor(5)
pla1, pla2 = Player(), Player()
game = OddsEvens(pla1, pla2)
print(game)
print(game.play())
print(game.results())
