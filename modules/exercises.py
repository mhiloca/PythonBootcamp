import math
from keyword import iskeyword
from random import *


def contains_keyword(*args):
    if any([w for w in args if iskeyword(w)]):
        return True
    else:
        return False


answer = math.sqrt(15129)
print(answer)
print(iskeyword('is'))
print('- ' * 5)
words = 'exercise', 'clothes', 'if'
print(contains_keyword(*words))
print(iskeyword('if'))
print(randint(1, 10))
