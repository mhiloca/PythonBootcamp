def decor(n):
    print('- ' * n)


class Student:
    def __init__(self):
        self.first = input('Name: ').title().strip()
        self.last = input('Surname: ').title().strip()
        self.grade()

    def __repr__(self):
        return f'{self.fullname():.<25}{self.grades}{self._final_grade():.>15}'

    def fullname(self):
        return self.first+' '+self.last

    def grade(self):
        self.grades = []
        c = 0
        while c < 2:
            try:
                g = float(input('Grade: '))
                self.grades.append(g)
                c += 1
            except ValueError:
                print('\033[31mInvalid grade\033[m')

    def _final_grade(self):
        sum_grades = sum(self.grades)
        final = sum_grades / len(self.grades)
        return final


class Report:
    def __init__(self):
        self.report = []
        while True:
            self.report.append(Student())
            while True:
                ans = input('Would you like to register another student? ').strip().upper()[0]
                if ans not in 'NY':
                    print('\033[31mInvalid answer\033[m')
                else:
                    break
            if ans == 'N':
                break

    def __repr__(self):
        return f'{self.report}'

    def show(self):
        for i in self.report:
            print(i)

    def specific(self, full_name):
        for i in self.report:
            if full_name == i.fullname():
                print(i)


grade_report = Report()
decor(25)
print(f'{"GRADE REPORT":^50}')
decor(25)
grade_report.show()
decor(15)
fn = input('Student fullname: ').title().strip()
decor(15)
grade_report.specific(fn)
