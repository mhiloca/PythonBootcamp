def decor(n):
    print('- ' * n)


class Student(dict):
    def __init__(self):
        super().__init__()
        decor(10)
        first = input('First name: ').title().strip()
        last = input('Surname: ').title().strip()
        self['name'] = first+' '+last
        self['grades'] = self._grades()

    def __repr__(self):
        return super().__repr__()

    def _grades(self):
        grades = []
        while True:
            try:
                g = float(input('Grade: '))
                grades.append(g)
            except ValueError:
                print('\033[31mInvalid value\033[m')
            while True:
                decor(5)
                ans = input('Another grade? ').strip().upper()[0]
                if ans not in 'NY':
                    print('\033[31mInvalid answer\033[m')
                else:
                    break
            if ans == 'N':
                break
        return grades


class Group(list):
    def __init__(self):
        super().__init__()
        while True:
            self.append(Student())
            while True:
                decor(20)
                ans = input('Register another student? ').strip().upper()[0]
                if ans not in 'NY':
                    print('\033[31mInvalid answer\033[m')
                else:
                    break
            if ans == 'N':
                break

    def __repr__(self):
        return super().__repr__()


class Analyses(dict):
    def __init__(self, group):
        super().__init__()
        self.group = group
        self['students'] = self._students()
        self['greater grade'] = self._greater_grade()
        self['avarage grade'] = self._avarage_grade()
        self['situation'] = self._situation()

    def __repr__(self):
        return super().__repr__()

    def _students(self):
        return len(self.group)

    def _greater_grade(self):
        return max(max(self.group, key=lambda x: x['grades'])['grades'])

    def _least_grade(self):
        return min(min(self.group, key=lambda x: x['grades'])['grades'])

    def _avarage_grade(self):
        soma = sum(map(lambda x: sum(x['grades']), self.group))
        avarage = soma / sum([len(x['grades']) for x in self.group])
        return round(avarage, 1)

    def _situation(self):
        if self['avarage grade'] < 7:
            return 'BAD'
        return 'GOOD'


team1 = Group()
decor(20)
decor(20)
print(Analyses(team1))
