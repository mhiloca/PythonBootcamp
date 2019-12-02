from datetime import date


class Worker:
    def __init__(self):
        self.name = input('Name: ')
        while True:
            try:
                birthyear = int(input('Birthyear: '))
                actual = date.today().year
                self.age = actual - birthyear
                break
            except ValueError:
                print('\033[31mInvalid year\033[m')
        while True:
            try:
                self.ctps = int(input('CTPS number: '))
                break
            except ValueError:
                print('\033[31mInvalid year\033[m')
        while True:
            gender = input('Gender: ').strip().upper()[0]
            if gender not in 'MF':
                print('\033[31mInvalid gender\033[m')
            else:
                if gender == 'F':
                    self.gender = 'FEMALE'
                    break
                else:
                    self.gender = 'MALE'
                    break
        if self.ctps != 0:
            self._ctps_regist()

    def __repr__(self):
        if self.ctps == 0:
            return f'{self.name:<20}{self.age:<10}{self.gender:>5}'
        else:
            return f'{self.name}: {self.age} years old - {self._retire():} ' \
                f'years to retirement at {self._salary()}/month'

    def _ctps_regist(self):
        while True:
            try:
                self.contract = int(input('Contract Year: '))
                break
            except ValueError:
                print('\033[31mInvalid year\033[m')
        while True:
            try:
                self.salary = float(input('Monthly Wages: '))
                break
            except ValueError:
                print('\033[31mInvalid value\033[m')

    def _retire(self):
        if self.gender == 'MALE':
            remains = 65 - self.age
        else:
            remains = 60 - self.age
        return remains

    def _salary(self):
        return f'{round(self.salary * 0.75, 2)}'


workman = Worker()
print(workman)
