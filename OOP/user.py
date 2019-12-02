class User:

    active_users = 0

    @classmethod
    def display_act_users(cls):
        return f'There are currently {cls.active_users} active users'

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(',')
        return cls(first, last, int(age))

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def __repr__(self):
        return f'{self.full_name()} is {self.age} years old'

    def logout(self):
        User.active_users -= 1
        return f'{self.first} has logged out'

    def full_name(self):
        return f'{self.first}{self.last}'

    def initials(self):
        return f'{self.first[0]}.{self.last[0]}.'

    def likes(self, thing):
        return f'{self.initials()} likes {thing}'

    def is_adult(self):
        return self.age >= 18

    def birthday(self):
        self.age += 1
        return f'Happy {self.age}th, {self.initials()} !'


print(User.display_act_users())
user1 = User('Joe', 'Steele', 34)
user2 = User('Mary', 'Loo', 12)
print(user1.likes('ice cream'))
print(user2.likes('chocolate'))
print(user1.is_adult())
print(user2.is_adult())
print(user1.birthday())
user3 = User('Tavinho', 'Cabezita', 40)
print(User.display_act_users())
print(user1.logout())
print(User.active_users)
print(User.display_act_users())
user4 = User.from_string('Mhirley, Lopes, 40')
print(user4.full_name())
print(user4.is_adult())
print(user4)

