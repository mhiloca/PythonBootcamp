class Chicken:

    total_eggs = 0

    def __init__(self, name, species, eggs=0):
        self.name = name
        self.species = species
        self.eggs = eggs
        Chicken.total_eggs += self.eggs

    def __repr__(self):
        return f'{self.name} is a {self.species}'

    def get_eggs(self):
        return f'{self.name} has {self.eggs} egg(s) now'

    def lay_egg(self):
        self.eggs += 1
        Chicken.total_eggs += 1
        return self.eggs


c1 = Chicken('Marilu', 'galinha')
c2 = Chicken('Renata', 'galinha')
print(Chicken.total_eggs)
c2.lay_egg()
print(c2.get_eggs())
c2.lay_egg()
c1.lay_egg()
c2.lay_egg()
print(c2.get_eggs())
print(c1.get_eggs())
print('- ' * 15)
print(Chicken.total_eggs)
