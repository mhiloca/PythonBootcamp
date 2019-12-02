from csv import DictReader
from random import choice
from validate import play


def line(n):
    print('- ' * n)


def get_quote(csv_file):
    with open(csv_file) as file:
        reader = DictReader(file)
        quotes = list(reader)
    for quote in quotes:
        if quote['text'] == 'text':
            quotes.remove(quote)
        elif quote['author'] == 'George Bernard Shaw':
            quote['hint_gender'] = 'The author is a man'
    return quotes


def play_game(quotes):
    quote = choice(quotes[1:])
    print('Here is a quote: ' + quote['text'])
    count = 3
    line(10)
    guess = input('Do you know who said this? ').strip().title()
    while count > 0:
        if guess.lower() == quote['author'].lower():
            break
        else:
            line(5)
            print_hint(count, quote)
            guess = input(f'Try once again, you have {count} guesses: ')
            count -= 1
    line(10)
    if count == 0 and guess.lower() != quote['author'].lower():
        print(f'Not this time. The author is {quote["author"]}')
    else:
        print('You got it! Well done.')
    line(15)
    if play() == 'N':
        line(15)
        print('END OF GAME')
    else:
        line(15)
        play_game(quotes)


def print_hint(count, quote):
    if count == 3:
        print('Here is a hint for you: ' + quote['hint_born'])
    elif count == 2:
        print(f'Not yet, another hint for you:\n'
              f'The author initials are '
              f'{quote["author"].split()[0][0]} '
              f'{quote["author"].split()[1][0]}\n'
              f'And byt the way... {quote["hint_gender"]}')
    elif count == 1:
        print(f'Last hint! A bit of the author\'s history:\n'
              f'{quote["hint_text"]}')


csv_file = 'quotes_file.csv'
line(15)
play_game(get_quote(csv_file))
