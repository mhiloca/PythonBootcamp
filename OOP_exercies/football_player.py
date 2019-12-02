def decor(n):
    print('- ' * n)


err = '\033[31mInvalid value\033[m'


class Player(dict):
    def __init__(self):
        super().__init__()
        self['name'] = input('Name: ').title().strip()
        while True:
            try:
                self['matches'] = int(input('Played matches: '))
                break
            except ValueError:
                print(err)
        if self['matches'] != 0:
            self._goals()

    def __repr__(self):
        return super().__repr__()

    def _goals(self):
        self['goals'] = []
        for i in range(self['matches']):
            try:
                goals = int(input(f'Goals match {i+1}: '))
                self['goals'].append(goals)
            except ValueError:
                print(err)


class Files(list):
    def __init__(self):
        super().__init__()
        while True:
            decor(15)
            self.append(Player())
            while True:
                ans = input('Register another player? ').strip().upper()[0]
                if ans not in 'NY':
                    print(err)
                else:
                    break
            if ans == 'N':
                break

    def _keys(self):
        decor(40)
        for key in self[0].keys():
            print(f'{key.upper():<20}', end='')
        print()

    def show_all(self):
        self._keys()
        for i in self:
            for value in i.values():
                if not isinstance(value, list):
                    print(f'{value:<20}', end='')
                else:
                    print(value)

    def show_specific(self):
        while True:
            while True:
                decor(5)
                answer = input('Check status: ').strip().upper()[0]
                if answer not in 'NY':
                    print(err)
                else:
                    break
            if answer == 'N':
                break
            else:
                while True:
                    name = input('Player\'s name: ').title().strip()
                    if filter(lambda x: x['name'] == name, self):
                        self._keys()
                        for i in self:
                            if i['name'] == name:
                                for v in i.values():
                                    if not isinstance(v, list):
                                        print(f'{v:<20}', end='')
                                    else:
                                        print(v)
                        break
                    else:
                        print('\033[31mPlayer not found\033[m')


players = Files()
players.show_all()
players.show_specific()
