from bs4 import BeautifulSoup
from csv import DictReader
from requests import get
from random import choice
from validate import play

URL = 'http://quotes.toscrape.com'


def get_quotes():
    with open('quotes.csv') as file:
        csv_r = DictReader(file)
        return list(csv_r)


def start_game(lista):
    while True:
        quo = choice(lista)
        print('= ' * 15)
        print(f'Here\'s a quote: \n{quo["text"]}')
        count, guess = 4,  ''
        print('Who said this?', end=' ')
        while count > 0:
            guess = input(f'Guess remaing {count}: ')
            print('- ' * 5)
            if guess.lower() == quo['author'].lower():
                print('You got it! Congratulations!')
                break
            count -= 1
            print_hint(quo, count)
        print('- ' * 10)
        if play() == 'N':
            break


def print_hint(quo, count):
    if count == 3:
        print('Here is a hint: ', end='')
        resp = get(URL + quo['link'])
        born = BeautifulSoup(resp.text, 'html.parser')
        print('The author was born on ', end='')
        date = born.find(class_='author-born-date').get_text()
        local = born.find(class_='author-born-location').get_text()
        print(date + ' ' + local)
    elif count == 2:
        print(f'Here is another hint: The author first name begins with a {quo["author"][0]}')
    elif count == 1:
        print(f'Last hint! The author\'s last name begins with a {quo["author"].split()[1][0]}')
    else:
        print(f'You didn\'t get this time, maybe next...\nThe author\'s name is: {quo["author"]}')


quotes = get_quotes()
start_game(quotes)
