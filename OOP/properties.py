class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError
    @property
    def full_name(self):
        return f'{self.first} {self.last}'

    @full_name.setter
    def full_name(self, name):
        self.first, self.last = name.split(' ')


jane = Human('Jane', 'Goodall', 90)
print(jane.age)
while True:
    try:
        jane.age = int(input('Enter new age: '))
        break
    except ValueError:
        print('Invalid age. Try again')
print(jane.age)
print(jane.full_name)
jane.full_name = 'Jane Lovegood'
print(jane.full_name)
