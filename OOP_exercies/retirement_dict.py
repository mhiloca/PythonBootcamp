from datetime import date


def decor(n):
    print('= ' * n)


def title(msg):
    print('- ' * 20)
    print(f'{msg:^40}')
    print('- ' * 20)


actual = date.today().year
err = '\033[31mInvalid value\033[m'


class Worker(dict):
    def __init__(self):
        super().__init__()
        first = input('First name: ').title().strip()
        last = input('Surname: ').title().strip()
        self['name'] = first+' '+last
        while True:
            try:
                birthyear = int(input('Birthyear: '))
                self['age'] = actual - birthyear
                break
            except ValueError:
                print(err)
        while True:
            gender = input('Gender: ').upper().strip()[0]
            if gender not in 'MF':
                print(err)
            else:
                if gender == 'F':
                    self['gender'] = 'female'
                    break
                else:
                    self['gender'] = 'male'
                    break
        while True:
            try:
                self['ctps'] = int(input('CTPS number: '))
                break
            except ValueError:
                print(err)
        if self['ctps'] != 0:
            self._ctps_reg()

    def __repr__(self):
        return super().__repr__()

    def _ctps_reg(self):
        while True:
            try:
                self['contract'] = int(input('Contract year: '))
                break
            except ValueError:
                print(err)
        if self['gender'] == 'female':
            self['remains'] = 60 - self['age']
        else:
            self['remains'] = 65 - self['age']


class File(list):
    def __init__(self):
        super().__init__()
        while True:
            title('WORKER')
            self.append(Worker())
            while True:
                ans = input('Register another person? ').strip().upper()[0]
                if ans not in 'NY':
                    print(err)
                else:
                    break
            if ans == 'N':
                break

    def _keys(self):
        for i in self[0].keys():
            print(f'{i.upper():<20}', end='')
        print()

    def show(self):
        decor(40)
        self._keys()
        for i in self:
            for v in i.values():
                print(f'{v:<20}', end="")
            print()

    def specific(self, name):
        decor(40)
        self._keys()
        for i in self:
            if i['name'] == name:
                for v in i.values():
                    print(f'{v:<20}', end="")


files = File()
files.show()
work = input('Check status: ').strip().title()
files.specific(work)
