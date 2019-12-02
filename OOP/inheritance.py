class Animal:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    # def __repr__(self):
    #     return f'{self.name} is a {self.species}'

    def make_sound(self, sound):
        return f'{self} makes {sound}'


class Cat(Animal):

    def __init__(self, name, species, breed, toy):
        super().__init__(name, species)
#        Animal.__init__(self, name, species)
        self.breed = breed
        self.toy = toy

    def play(self):
        return f'{self.name} loves to play with {self.toy}'


an1 = Cat('Blue', 'cat', 'Scottish Fold', 'string')
print(an1)
print(an1.breed)
print(an1.toy)
print(an1.play())
