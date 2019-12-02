class Expression:
    def __init__(self):
        self.expr = input('Math expression: ')

    def validate(self):
        pile = []
        for i in self.expr:
            if i == '(':
                pile.append('(')
            elif i == ')':
                if len(pile) > 0:
                    pile.pop()
                else:
                    pile.append('(')
        if len(pile) == 0:
            return True
        return False


math = Expression()
print(math.validate())

