from random import choice


class Player:

    move = ''

    def __init__(self, name):
        try:
            name = int(name)
            if name == 1:
                name = input('Enter Player2 name: ').title()
                self.name = name
            else:
                self.name = 'Computer'
        except (ValueError, TypeError):
            self.name = name

    def __repr__(self):
        return f'Player {self.name}'


class Game:

    m1 = m2 = ''

    def __init__(self, pl1, pl2):
        self.pl1 = pl1
        self.pl2 = pl2

    def __repr__(self):
        return f'{self.pl1} X {self.pl2}'

    def play(self, pl):
        moves = 'ROCK', 'PAPER', 'SCISSORS'
        if pl == self.pl2:
            if self.pl2.name == 'Computer':
                m2 = choice(moves)
                Game.m2 = m2
                return Game.m2
            else:
                while True:
                    m2 = input(f'What is your move ({self.pl2})? ').upper().strip()
                    if m2 not in moves:
                        print('\033[31mInvalid move\033[m')
                    else:
                        Game.m2 = m2
                        return Game.m2
        else:
            while True:
                m1 = input(f'What is your move ({self.pl1})? ').upper().strip()
                if m1 not in moves:
                    print('\033[31mInvalid move\033[m')
                else:
                    Game.m1 = m1
                    return Game.m1

    def display_game(self, pl):
        if pl == self.pl1:
            return f'{self.pl1} plays {Game.m1}'
        return f'{self.pl2} plays {Game.m2}'

    @classmethod
    def _res(cls):
        win_mov = ''
        game = {Game.m1, Game.m2}
        if game == {'ROCK', 'PAPER'}:
            win_mov = 'PAPER'
        elif game == {'SCISSORS', 'PAPER'}:
            win_mov = 'SCISSORS'
        elif game == {'SCISSORS', 'ROCK'}:
            win_mov = 'ROCK'
        if Game.m1 == win_mov:
            los_mov = Game.m2
        else:
            los_mov = Game.m1
        return win_mov, los_mov

    def check_game(self):
        if Game.m1 == Game.m2:
            return "IT'S A TIE!"
        else:
            return f'{self._res()[0]} beats {self._res()[1]}\n{self._winner()} wins!'

    def _winner(self):
        if self._res()[0] == Game.m1:
            return self.pl1
        return self.pl2


def decor():
    print('- ' * 20)


decor()
print(f"LET'S PLAY ROCK, PAPER AND SCISSORS")
decor()
name1 = input("What's your name? ").title()
player1 = Player(name1)
name2 = input("Who are you playing against,\n"
              "[ 1 ] - Another player\n"
              "[ 2 ] - Computer\n"
              "Enter your opponent: ")
player2 = Player(name2)
decor()
game1 = Game(player1, player2)
print(game1)
decor()
game1.play(player1)
decor()
game1.play(player2)
decor()
print(game1.display_game(player1))
print(game1.display_game(player2))
decor()
print(game1.check_game())
