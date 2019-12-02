import termcolor as t
import pyfiglet as fig
import requests as req
from random import choice
nums = ('zero', 'one', 'two', 'three', 'four', 'five', 'six',
        'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
        'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twelve')
linha = '= ' * 35
t.cprint(linha, color='blue')
title = 'Silly Dad Jokes'
print(t.colored(fig.figlet_format(title), color='blue'))
t.cprint(linha, color='blue')
print()
print('Let me tell you a joke.', end=' ')
url = "https://icanhazdadjoke.com/search"
while True:
    topic = input('Give me a topic: ')
    if len(topic) < 3:
        print('Topics are not that short!')
        print()
    else:
        break
res = req.get(
    url,
    headers={'Accept': 'application/json'},
    params={'term': topic, 'limit': 1}
).json()
n = res['total_jokes']
joke = res['results']
if n == 1:
    print(f'I have {nums[n]} joke about {topic}. Here it is: ')
    print()
    print(f"-› {joke[0]['joke']}")
elif n < 1:
    print(f'I have {nums[n]} jokes about {topic}. Sorry!')
else:
    print(f'I have {nums[n]} jokes about {topic}. Here goes one:')
    print()
    print(f"-› {choice(joke)['joke']}")
print()
