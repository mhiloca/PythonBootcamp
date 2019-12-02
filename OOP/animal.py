class Animal:
    def speak(self):
        raise NotImplementedError('Subclass need to implement this medthod')


class Dog(Animal):
    def speak(self):
        return 'woof'


class Cat(Animal):
    def speak(self):
        return 'meow'


class Fish(Animal):
    pass


d = Dog()
print(d.speak())
f = Fish()
print(f.speak())
