class Robot:
    def __init__(self, name, battery=100, skills=[]):
        self.name = name
        self.battery = battery
        self.skills = skills

    def charge(self):
        self.battery = 100
        return self

    def say_name(self):
        if self.battery > 0:
            self.battery -= 1
            return f'BEEP BOOP BEEP BOOP. My name is {self.name.upper()}'
        return 'Low power, please charge and try again'

    def learn_skills(self, new_skill, cost_to_learn):
        if self.battery >= cost_to_learn:
            self.battery -= cost_to_learn
            self.skills.append(new_skill)
            return f'WHOAH. I KNOW {new_skill.upper()}'
        return 'Low power, please charge and try again'
