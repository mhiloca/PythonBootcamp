def decor(n):
    print('- ' * n)


class Registration(list):
    def __init__(self):
        super().__init__()
        cont = 1
        while True:
            decor(15)
            print(f'{"PERSON":>15} {cont}')
            decor(15)
            self.append(Person())
            cont += 1
            while True:
                decor(5)
                ans = input('Would you like to register '
                            'another person? ').upper().strip()[0]
                if ans not in 'NY':
                    print('\033[31mInvalid answer\033[m')
                else:
                    break
            if ans == 'N':
                break


class Person:
    def __init__(self):
        while True:
            try:
                self.age = int(input('Age: '))
                if self.age > 130 or self.age < 0:
                    print('\033[31mInvalid age\033[m')
                else:
                    break
            except ValueError:
                print('\033[31mInvalid value\033[m')
        genders = ('cis-woman', 'cis-man', 'trans-woman',
                   'trans-man', 'non-binary')
        while True:
            self.gender = input('Gender identity: ').lower().strip()
            if self.gender not in genders:
                print('\033[31mInvalid gender\033[m')
            else:
                break

    def __repr__(self):
        return f'{self.gender.title()} of {self.age} years old'


class Analyses:
    def __init__(self, file):
        self.file = file
        decor(15)
        print(self._adults())
        print(self._women())
        print(self._minimen())

    def __repr__(self):
        return f'{len(self.file)} people registered'

    def _adults(self):
        adu = len(list(filter(lambda x: x.age > 18, self.file)))
        return f'There are {adu} people of full age'

    def _women(self):
        wom = [x for x in self.file
               if x.gender == 'cis-woman'
               or x.gender == 'trans-woman']
        return f'There is/are {len(wom)} women registered'

    def _minimen(self):
        men = [x for x in self.file
               if x.age < 18 and x.gender == 'cis-man'
               or x.gender == 'trans-man']
        return f'There is/are {len(men)} young men registered'


file_num_1 = Registration()
Analyses(file_num_1)

