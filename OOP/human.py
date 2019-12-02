from copy import copy as c


class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f'Human named {self.first} {self.last} aged {self.age}'

    def __len__(self):
        return self.age

    def __add__(self, h1):
        if isinstance(h1, Human):
            return Human(first='Newborn', last=self.last, age=0)
        raise TypeError('You cannot add that')

    def __mul__(self, other):
        if isinstance(other, int):
            return [c(self) for x in range(other)]
        raise TypeError("Cannot multiply")


j = Human('Jenny', 'Larsen', 47)
k = Human('Kevin', 'Jones', 49)
print(j)
print(len(j))
print(j + k)
jes = (j * 3)
print(jes)
jes[1].first = 'Jessica'
print(jes)
triplets = (k + j) * 3
print(triplets)
