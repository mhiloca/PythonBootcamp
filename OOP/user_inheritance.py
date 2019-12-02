class User:
    active_users = 0

    @classmethod
    def display_act_users(cls):
        if cls.active_users == 1:
            return f'There is {cls.active_users} active user'
        return f'There are {cls.active_users} active users'

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(' ')
        return cls(first, last, int(age))

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self._age = age
        User.active_users += 1

    def __repr__(self):
        return self.full_name()

    def full_name(self):
        return f'{self.first} {self.last}'

    def logout(self):
        User.active_users -= 1
        return f'{self.first} has logged out'

    def is_senior(self):
        if self._age > 65:
            return True
        return False

    def initials(self):
        return f'{self.first[0]}.{self.last[0]}'

    def birthday(self):
        self._age += 1
        return f'Happy {self._age}th, {self.first}!'

    def likes(self, thing):
        return f'{self.first} likes {thing}'


class Moderator(User):

    total_mods = 0

    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community
        Moderator.total_mods += 1

    @classmethod
    def display_act_mods(cls):
        if cls.total_mods == 1:
            return f'There is {cls.total_mods} active moderator'
        return f'There are {cls.total_mods} active moderators'

    @classmethod
    def from_an_str(cls, data_str):
        first, last, age, community = data_str.split(' ')
        return cls(first, last, int(age), community)

    def remove_post(self):
        return f'{self.full_name()} removed a post from the {self.community} community'


user1 = User.from_string("Gustavo Cabeza 40")
print(User.display_act_users())
mod1 = Moderator.from_an_str("Mhirley Lopes 40 family")
print(Moderator.display_act_mods())
print(User.display_act_users())
