class User:

    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greetings(self):
        return f'Hello, my name is {self.name} and I am {self.age} years old'


class Customer(User):
    def __init__(self, name, email, age, balance):
        super().__init__(name, email, age)
        self.balance = balance

    def greetings(self):
        return f'{User.greetings(self)} and I have a balance of {self.balance}'


john = Customer('John Doe', 'john@gmail.com', 40, 500)
print(john.greetings())
print()
